#!/usr/bin/python3
""" Lockboxes"""
from collections import deque


def canUnlockAll(boxes):
    """Lockboxes"""
    n = len(boxes)
    unlocked = set([0])
    keys = deque([0])  # Use a deque for more efficient popping from the left

    while keys:
        key = keys.popleft()  # Efficiently pop from the left
        for k in boxes[key]:
            if k not in unlocked and k < n:
                unlocked.add(k)
                keys.append(k)

    return len(unlocked) == n
