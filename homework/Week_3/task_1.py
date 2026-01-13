'''
Task 1.
1. Write a program to calculate the area of various geometric shapes.
2. Given 3 different arrays of integers (the size of each does not exceed 15). In
each array, find the sum of the elements and the arithmetic mean.'''

import math

print("Task 1.1")

def area_circle(r):
    return 3.14 * r * r

def area_rect(a, b):
    return a * b

def area_triangle(base, h):
    return 0.5 * base * h

a = float(input("Enter your side a: "))
b = float(input("Enter your side b: "))
r = float(input("Enter your radius: "))
base = float(input("Enter your base to triange"))
h = float(input("Enter your height to triange "))

print("Circle:", area_circle(r))
print("Square:", area_rect(a, b))
print("Triangle:", area_triangle(base, h))


print("\n Task 1.2")

def create_array(number):
    print(f"\nEntering array number {number}")
    size = int(input("How many elements (not more than 15)? "))
    
    new_arr = []
    for i in range(size):
        val = int(input(f"  Enter number {i+1}: "))
        new_arr.append(val)
    return new_arr

def print_stats(arr):
    if len(arr) == 0:
        print("Array enpty!")
        return
        
    s = sum(arr)
    avg = s / len(arr)
    print(f"Your array: {arr}")
    print(f"Sum: {s}, Average: {avg:.2f}")

arr1 = create_array(1)
arr2 = create_array(2)
arr3 = create_array(3)


print("\n Result")
print_stats(arr1)
print_stats(arr2)
print_stats(arr3)