'''
Task 3. Given a real number A containing two decimal places and two after. Get a
new number by changing the integer and fractional parts in the number A.
Let's try to find the integer and fractional parts of the number. And then just collect
a new number, increasing the fractional part by 100 times and reducing the whole
part by 100 times too
'''

a = float(input('Enter a number: '))

integer = int(a)
fractional = a - integer

new_number = round((fractional * 100) + (integer / 100), 2)

print(new_number)