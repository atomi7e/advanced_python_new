'''
Task 5.
1. Two fractions A/B and C/D are given (A, B, C, D are natural numbers). Write a
program to subtract the second fraction from the first fraction. The answer must be
an irreducible fraction. Use a subroutine of the Euclid algorithm to determine the
gcd.
2. Write a program that prints all the divisors of the given number in one line,
separating them with spaces.
'''

print("Task 5.1")

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

res_top = (A * D) - (C * B)
res_bottom = B * D

if res_top == 0:
    print("Result: 0")
else:
    common = gcd(res_top, res_bottom)
    print(f"Result: {res_top // common}/{res_bottom // common}")


print("\nTask 5.2")

num = int(input("Enter your number: "))
print(f"Divisors of a number {num}:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()