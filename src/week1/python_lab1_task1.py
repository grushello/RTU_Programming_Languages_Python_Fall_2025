"""
Task 1 – Simple Function with Arithmetic
---------------------------------------
Write a function `circle_area(radius)` that returns the area of a circle.
Formula: area = π × radius²
Use the math module for π.
Ask user for radius and print result with 2 decimals.
"""

import math


def circle_area(radius):
    return math.pi * radius**2


if __name__ == "__main__":
    radius = input("Enter the radius, please ")
    area = circle_area(float(radius))
    print(f"area of a circle: {area : .2f}")
    pass
