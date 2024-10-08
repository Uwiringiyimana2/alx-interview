#!/usr/bin/python3
"""Recursive technique"""


def countdown(i):
    """infinite loop"""
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)


if __name__ == "__main__":
    countdown(3)