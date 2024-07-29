def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set([0])  # Start with the first box unlocked
    keys = [0]  # Start processing keys from the first box

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == n

# Example usage
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Output: False

