#!/usr/bin/python3
"""
check if all boxes are opened or not
"""


def canUnlockAll(boxes):
    """
    we are gonna check all if all boxes
    can be opened or not by opening each
    box and get all the keys from the box
    after that we are gonna use those keys
    to open other boxes after we finish all
    key in our set and there are some boxes
    which are not open the function will return
    False but if we opened all boxes using the keys
    in the set the function will return True
    """
    num_boxes = len(boxes) - 1
    length = num_boxes + 1


    while True:
        if num_boxes != 0 and boxes[0]:
            element = boxes[0].pop(0)
        else:
            break

        if element == None:
            continue

        if element != 0 and element < length and boxes[element] != 1:
            if len(boxes[element]) == 0:
                boxes[0].append(None)
            else:
                for ele in boxes[element]:
                    boxes[0].append(ele)
            boxes[element] = 1
            num_boxes -= 1


    if num_boxes == 0:
        return True
    else:
        return False
