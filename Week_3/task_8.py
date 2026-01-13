'''
Task 8.
1. Find all natural numbers not exceeding the given n that are divisible by each of
their digits.
2. Enter a one-dimensional array A of length m. Swap the first and last elements in
it. Enter the length of the array and its elements from the keyboard. In a program,
describe a procedure for replacing elements of an array. Output the original and
resulting arrays.
'''
print("Task 8.1")

def check_digits(num):
    temp = num
    while temp > 0:
        digit = temp % 10 
        
        if digit == 0:
            return False
        
        if num % digit != 0:
            return False
            
        temp = temp // 10
    return True

n = int(input("Enter number N: "))
print("Matching numbers:")

for i in range(1, n + 1):
    if check_digits(i):
        print(i, end=" ")
print()


print("\nTask 8.2")

def swap_elements(arr):
    if len(arr) == 0:
        return
    
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp

m = int(input("Enter array size: "))
my_array = []

print("Enter numbers:")
for i in range(m):
    val = int(input(f"  Element {i+1}: "))
    my_array.append(val)

print("Original:", my_array)
swap_elements(my_array)
print("Result:", my_array)