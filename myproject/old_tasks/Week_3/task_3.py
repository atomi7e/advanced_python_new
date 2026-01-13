'''
Task 3.
1. The legs of two right triangles are given. Write a function to calculate the length
of the hypotenuse of these triangles. Compare and deduce which of the
hypotenuses is greater and which is smaller.
2. Convert a string so that the letters of each word in it are sorted alphabetically.
'''

import math

print("Task 3.1")

def hypotenuse(a,b):
    return math.sqrt(a**2 + b**2)

a = float(input("Enter your side a: "))
b = float(input("Enter your side b: "))
c = float(input("Enter your side c: "))
d = float(input("Enter your side d: "))

h1 = hypotenuse(a, b)
h2 = hypotenuse(c, d)

if h1 > h2:
    print("First more")
elif h2 > h1:
    print("Second more")
else:
    print("There are equal")

print("\nTask 3.2")

text = input("Enter your text: ")
words = text.split()
result_text = ""

for word in words:
    letters = list(word)
    
    letters.sort()
    
    new_word = ""
    for char in letters:
        new_word = new_word + char

    result_text = result_text + new_word + " "

print("Result:", result_text)