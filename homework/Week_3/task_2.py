'''
Task 2.
1. Calculate the area of a regular hexagon with side a using the triangle area
subroutine.
2. The user enters two sides of three rectangles. Bring out their area.
'''

import math

print("Task 2.1")

def triangle_area(a):
    return (math.sqrt(3) / 4) * (a ** 2)

def hexagon_area(a):
    return 6 * triangle_area(a)

side = float(input("Enter your side of hexagon: "))
print(f"Side: {side}, Area: {hexagon_area(side)}")

print("\nTask 2.2")

for i in range(3):
    print(f"Rectangle number {i+1}")
    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    print("Area:", a * b)