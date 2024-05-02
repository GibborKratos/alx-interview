#!/usr/bin/python3
'''0x01. Lockboxes
'''

def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    keys = set([0])  # Initialize with the key to the first box
    visited = set()

    while keys:
        box = keys.pop()
        visited.add(box)
        for key in boxes[box]:
            if key < n and key not in visited:
                keys.add(key)

    return len(visited) == n

