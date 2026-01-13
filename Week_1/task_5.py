'''Task 5. To create a program for guessing the intended number using a computer.
The computer prompts the performer to perform the following actions and enter
the result:
a) multiply the planned number by 5;
b) add 8;
c) multiply the sum by 2.
Based on the entered result, the computer determines the number and prints it on
the screen. '''

num = int(input('Enter a number: '))
result = ((num /2) - 8) /2
print(result)