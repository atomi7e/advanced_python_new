'''
Task 7.
1. Numbers X, Y, Z, T are given — the lengths of the sides of the quadrilateral.
Calculate it
area if the angle between sides of length X and Y is a right angle. Use two routines
to calculate areas: a right triangle and a rectangle.
2. Write a program that converts a non-negative integer given to it into a 10-digit
octal code, preserving leading zeros.
'''

import math

print("Task 7.1")

def triangle_right(a, b):
    return 0.5 * a * b

def heron(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

X = int(input("X: "))
Y = int(input("Y: "))
Z = int(input("Z: "))
T = int(input("T: "))

area1 = triangle_right(X, Y)

diag = math.sqrt(X**2 + Y**2)

area2 = heron(Z, T, diag)

print("Area:", area1 + area2)

print("\nTask 7.2")

n = int(input("Enter your number: "))

octal_str = f"{n:06o}"
print(f"Число {n} в коде: {octal_str}")