'''Task 2. A department has three employees, and their salaries are paid in tenge. The
goal is to determine the difference between the salary of the highest-paid employee
and the lowest-paid employee. (2 points)
Input Data
Contains the salaries of all employees, separated by spaces. Each salary is a natural
number not exceeding 10!,
Output Data
The output must contain a single integer—the difference between the maximum
and minimum salaries.
Example
input output
100 500 1000 900
36 11 20 25
'''

a = int(input('first salary: '))
b = int(input('second salary: '))
c = int(input('third salary: '))

if a > b and a > c and b> c:
    print(a - c)
elif b > a and b > c and a > c:
    print(b-c)
elif c > a and c > b and a > b:
    print(c-b)
elif a > b and a > c and c > b:
    print(a-b)
elif b > a and b > c and c > a:
    print(b-a)
elif c > a and c > b and b > a:
    print(c-a)
