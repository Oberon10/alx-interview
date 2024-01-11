#!/usr/bin/python3
"""
0. Lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes: List of lists representing locked boxes.

    Returns:
    - True if all boxes can be opened, else False.
    """
    # Set to keep track of opened boxes
    opened_boxes = set()

    # Add the first box to the set
    opened_boxes.add(0)

    # Queue to keep track of boxes to be checked
    box_queue = [0]

    while box_queue:
        current_box = box_queue.pop(0)

        # Check if the keys in the current box open new boxes
        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                box_queue.append(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
