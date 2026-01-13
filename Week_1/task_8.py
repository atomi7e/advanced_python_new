'''
Add a division by zero check to the previous task.
Write down the verification using the abbreviated form of the condition.
Task 8 - A little game (1 points)
Ask the user to enter a word, as well as a number. Use loops to output each
character of the string, and the character must be repeated the number of times
equal to the number that the user entered. Each subsequent new character must be
output from a new line, for example:
Hello# What the user entered
3 # The number that the user entered # Result
HHH
eee
lll
lll
ooo
'''
word = input('Enter a word: ')
number = int(input('Enter a number: '))

for i in range(len(word)):
    print(word[i] * number)

