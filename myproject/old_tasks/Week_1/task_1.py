'''
Task 1. Write a program that would ask the user: (1 points)
First name, Last Name, Age, Phone number
- Last name, first name ("Your last name, first name?") - age ("How old are you?")
- phone number ("Your phone number?")
After that would output three lines:
"Your first name, last name"
"Your age"
"Your phone number"
'''

name = input("Enter your first name: ")
surname = input("Enter your last name: ")
age = input("How old are you? ")
phone = input("Enter your phone number: ")

print("Your first name, last name", name, surname)
print("Your age", age)
print("Your phone number", phone)