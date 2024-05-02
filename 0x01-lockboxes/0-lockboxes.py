#!/usr/bin/python3
"""Script will unlock list of lists"""


def canUnlockAll(boxes):
    if not boxes:
        return False
    
    n = len(boxes)
    visited = set()
    queue = [0]  # Start with box 0
    
    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)
        
        keys = boxes[current_box]
        for key in keys:
            if key < n and key not in visited:
                queue.append(key)
    
    return len(visited) == n

# Example usage:
boxes = [
    [1],     # Box 0 contains key to Box 1
    [2],     # Box 1 contains key to Box 2
    [3],     # Box 2 contains key to Box 3
    [],      # Box 3 has no key
]
print(canUnlockAll(boxes))  # Output: True

