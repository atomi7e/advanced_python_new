'''Task 4. It is required to calculate the sum of integers located between the numbers
1 and N inclusive. (2 points)
Input Data contains a single integer N, whose absolute value does not exceed 10".
Output Data must contain a single integer - the sum of the numbers between 1 and
N, inclusive.
input output
5 15'''
number = int(input('Enter a number: '))

sum = 0
for i in range(number+1):
    sum += i

print(sum)