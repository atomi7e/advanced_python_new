'''
Task 4.
1. Two fractions A/B and C/D are given (A, B, C, D are natural numbers). Write a
program for dividing a fraction by a fraction. The answer must be an irreducible
fraction. Use a subroutine of the Euclid algorithm to determine the gcd.
2. Given a circle (xa)2 + (yb)2 = R2 and points Р(р1, р2), F(f1, f1), L(l1,l2). Find
out and display on the screen how many points lie inside the circle. Checking
whether a point lies inside a circle should be done in the form of a procedure
'''
print("Task 4.1")

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

print("Enter A and B:")
A = int(input("A: "))
B = int(input("B: "))

print("Entetr C and D:")
C = int(input("C: "))
D = int(input("D: "))

new_top = A * D
new_bottom = B * C


common = gcd(new_top, new_bottom)
print(f"Result: {new_top // common}/{new_bottom // common}")


print("\nTask 4.2")

def check_point(x, y, r):
    if (x**2 + y**2) <= r**2:
        print(f"  Point ({x}, {y}) is inside")
        return 1
    else:
        print(f"  Point ({x}, {y}) is outside")
        return 0

R = int(input("Enter your radius: "))
count = 0

for i in range(3):
    print(f"\nPoint #{i+1}")
    x = int(input("Enter point x: "))
    y = int(input("Enter point y: "))
    
    count += check_point(x, y, R)

print("\nTotal inside points:", count)