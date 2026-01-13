'''
Task 6.
1. Write a program to find the greatest common divisor (GCD) and the least
common multiple (LCM) of two natural numbers LCM(A, B) = (A*B)/GCD(A,B).
Use a subroutine of the Euclid algorithm to determine the gcd.
2. Write a program to calculate the area of a convex quadrilateral given the lengths
of four sides and a diagonal.
'''
import math

print("Task 6.1")

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    return (a * b) // get_gcd(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Numbers: {num1}, {num2}")
print("GCD:", get_gcd(num1, num2))
print("LCM:", get_lcm(num1, num2))


print("\nTask 6.2")

def heron(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

s1 = int(input("Enter first side: "))
s2 = int(input("Enter second side: ")) 
s3 = int(input("Enter third side: ")) 
s4 = int(input("Enter fourt side: ")) 
diag = int(input("Enter your diagonal: "))                    

area1 = heron(s1, s2, diag) 
area2 = heron(s3, s4, diag) 

print("Overall result:", area1 + area2) 