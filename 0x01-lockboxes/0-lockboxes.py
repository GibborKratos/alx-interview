#!/usr/bin/python3
"""Script will unlock list of lists"""


def canUnlockAll(boxes):
    if not boxes:
        return False
    
    n = len(boxes)
    visited = set()
    
    def dfs(box):
        if box in visited:
            return
        visited.add(box)
        for key in boxes[box]:
            if key < n:
                dfs(key)
    
    dfs(0)  # Start DFS from box 0
    
    return len(visited) == n
print(canUnlockAll(boxes))  # Output: True

