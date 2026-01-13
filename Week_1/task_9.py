'''Task 9 Lucky ticket (1 points)
Do you use public transportation? You've probably paid for your ride and received
a ticket with a number. A lucky ticket is a ticket with a six-digit number, where the
sum of the first three digits equals the sum of the last three. So, a ticket with the
number 385916 is lucky, because 3 + 8 + 5 = 9 + 1 + 6. You need to write a
program that checks whether a ticket is lucky.
Example
input output
385916 YES
123456 NO'''

number = input('Enter a number: ')
if len(number) != 6:
    print('Error')
else:
    sum_1 = 0
    sum_2 = 0
    for i in range(3):
        sum_1 += int(number[i])
    for i in range(3, 6):
        sum_2 += int(number[i])
    if sum_1 == sum_2:
        print(number, 'YES')
    else:
        print(number, 'NO')