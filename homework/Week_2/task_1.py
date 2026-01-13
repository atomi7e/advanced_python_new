''' Task 1
You are given a sequence consisting only of the characters ‘>’, ‘<’, and ‘-’. Your
goal is to find the number of arrows hidden in this sequence. Arrows are substrings
of the form ‘>>-->’ and ‘<--<<’.
Input Data contains a string consisting of the characters '>', '<', and '-' (without
spaces). The string must be no more than 250 characters long.
Output Data
The desired number of arrows must be printed on a single line
'''
entered_value = str(input("Enter your string:"))

count = 0

for i in range(len(entered_value) - 4):
    if entered_value[i:i+5] == '>>-->':
        count += 1
    if entered_value[i:i+5] == "<--<<":
        count += 1

print("Counted data:", count)