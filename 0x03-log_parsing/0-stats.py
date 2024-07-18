#!/usr/bin/python3
"""Log parse"""
import sys
import signal
import re

# Initialize counters and variables
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

# Regular expression pattern to match the log format
log_pattern = re.compile(
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
)

def print_stats():
    """Function to print the statistics"""
    global total_file_size, status_code_counts
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)"""
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if not match:
            continue

        ip_address, date, status_code, file_size = match.groups()
        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        # Update total file size and status code counts
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        
        line_count += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
