"""
-----------------------------------------------------------------------
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
File: q4_rectangle_box.py
Creation Time: Oct 29th 2023 10:14 pm
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
"""


def solution(operations):
    maxW, maxH = 0, 0
    res = []

    for i in operations:
        w, h = i[1], i[2]
        if w > h:
            # Rotate 90-degrees to ensure the height is always more than width to match dimnesions
            w, h = h, w

        if i[0]:
            res.append(h >= maxH and w >= maxW)
        else:
            maxH = max(maxH, h)
            maxW = max(maxW, w)
    return res

def display_func(operations):
    print("\n")
    print(operations)
    print(solution(operations))

display_func([[1,1,1]])
display_func([[0,1,3],[0,4,2],[1,3,4],[1,3,2]])
display_func([[0,1,3],[0,4,2], [0,3,3],[1,3,4],[1,3,2]])
display_func([[0, 1, 3], [0, 2, 4], [1, 5, 2], [0, 1, 1], [1, 4, 1]])