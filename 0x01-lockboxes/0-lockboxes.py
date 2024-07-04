#!/usr/bin/python3
""" Lockboxes"""


def canUnlockAll(boxes):
    """Lockboxes"""
    n = len(boxes)
    unlocked = set()
    keys = set([0])

    while keys:
        key = keys.pop()
        if key not in unlocked:
            unlocked.add(key)
            for k in boxes[key]:
                if k not in keys:
                    keys.add(k)

    return len(unlocked) == n
