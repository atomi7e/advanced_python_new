'''Task 6 Smart Calculator (1 point)
Create a program that will receive actions from the user (+, -, *, /).
Depending on the action, the sum, difference, product or quotient of two numbers
specified by the user will be displayed.
For example:
"First number: 2" "Operation: -" "Second number: 3" 2 - 3 = -1'''

number_1 = int(input('Enter a number: '))
operation = input('Enter an operation: ')
number_2 = int(input('Enter a number: '))

if operation == '+':
    print(number_1 + number_2)
elif operation == '-':
    print(number_1 - number_2)
elif operation == '*':
    print(number_1 * number_2)
elif operation == '/':
    print(number_1 / number_2)