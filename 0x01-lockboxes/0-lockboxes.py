#!/usr/bin/python3
"""Defining a function called canUnlockAll"""


def appendKeys(availableKeys, box):
    """appends box keys to the available keys list"""
    for key in box:
        availableKeys.append(key)
    return availableKeys


def canUnlockAll(boxes):
    """returns True if all boxes can be opened else
    False"""
    availableKeys = boxes[0]
    openedBoxes = []
    currentBox = []
    for i, box in enumerate(boxes):
        if i == 0:
            continue
        for key in availableKeys:
            if key == i or key in box:
                currentBox = boxes[i]
                openedBoxes.append(currentBox)
                appendKeys(availableKeys, box)
                break

    for box in openedBoxes:
        boxes.remove(box)

    return True if len(boxes) == 1 else False
