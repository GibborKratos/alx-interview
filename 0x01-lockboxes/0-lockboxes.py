#!/usr/bin/python3

def canUnlockAll(boxes):
    """
	take boxes
		create set of keys
			go to box
			get all keys and add them setpfkeys
start opening boxes from setofkeys
go to each box of each key
		and take the keys from it and add them to set of keys
		keep looping through all setof key
			ignore keys that dont have box
		track opening of boxes by a counter, if at the en fit equals to length
		 of boxes it means all boxes unlock
  """
   length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        oldo = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if oldo != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
