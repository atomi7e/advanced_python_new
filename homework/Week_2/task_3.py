''' Task 3
The equation for fifth-graders is a string five characters long. The second character
is either a '+' (plus) or '-' (minus), and the fourth character is an '=' (equal) sign. Of
the first, third, and fifth characters, exactly two are digits from 0 to 9, and one is
the letter x, representing the unknown.
You are required to write a program that will solve this equation for x.
Input Output
x+5=7 2
3-x=9 -6
'''

eq = input().strip()

a, op , b, _ , c = eq

def val(x):
    return int(x) if x != "x" else None

A, B, C = val(a), val(b), val(c)

if op == "+":
    if A is None:
        print(C - B)
    elif B is None:
        print(C - A)
    else:
        print(A + B)
else:
    if A is None:
        print(C + B)
    elif B is None:
        print(A - C)
    else:
        print(A - B)