'''
-----------------------------------------------------------------------
File: doTheyBelong.py
Creation Time: Mar 30th 2024, 6:19 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

# All Test cases passed + Successfully submitted

def euclidean_distance(x1, y1, x2, y2):
    # calculate euclidean distance between two points on cartesian plane
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def calculate_area(x1, y1, x2, y2, x3, y3):
    # calculate the area of the triangle formed by three points
    return abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))

def do_they_belong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    # Check if the point 1 to 3 forms non-degenerate triangle
    a = euclidean_distance(x1, y1, x2, y2)
    b = euclidean_distance(x2, y2, x3, y3)
    c = euclidean_distance(x3, y3, x1, y1)
    if a + b <= c or b + c <= a or c + a <= b:
        return 0
    
    area = abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))

    # Calculate the area of the triangle formed by p and each side of the triangle
    area1 = calculate_area(x1, y1, x2, y2, xp, yp)
    area2 = calculate_area(x1, y1, xp, yp, x3, y3)
    area3 = calculate_area(xp, yp, x2, y2, x3, y3)

    # Calculate the area of the triangle formed by q and each side of the triangle
    area4 = calculate_area(x1, y1, x2, y2, xq, yq)
    area5 = calculate_area(x1, y1, xq, yq, x3, y3)
    area6 = calculate_area(xq, yq, x2, y2, x3, y3)

    # Check if p and/or q is inside the triangle
    p_inside = area == area1 + area2 + area3
    q_inside = area == area4 + area5 + area6

    # Return the correct scenario number
    if p_inside and q_inside:
        return 3
    elif p_inside:
        return 1
    elif q_inside:
        return 2
    else:
        return 4

    pass

print(do_they_belong(3,1,7,1,5,5,3,1,0,0)) # 1
print(do_they_belong(0,0,2,0,4,0,2,0,4,0)) # 0


# A point belongs to a triangle if it lies somewhere on or inside the triangle. Given two points p = (xp, yp) and q = (xq, yq), return the correct scenario number:
        # 0: If the triangle abc does not form a valid non-degenerate triangle.
        # 1: If point p belongs to the triangle but point q does not.
        # 2: If point q belongs to the triangle but point p does not.
        # 3: If both points pand belong to the triangle.
        # 4: If neither point p nor point q belong to the triangle.
    # Calculate the area of the triangle