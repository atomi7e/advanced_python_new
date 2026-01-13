# Task 1: Temperature Conversion
'''
c = int(input("Enter the temperature in Celsius: "))

def changingTypeOfTemperature(temp):
    print ("Temperature in F: ",((9/5)* temp)+32)

changingTypeOfTemperature(c)
'''
# Task 2: Basic Calculator
'''a = int(input("enter a number: "))
b = int(input("enter another number: "))
d = input("What do you want? +, -, *, / ")

if d == "+":
    print(a+b)
elif d == "-":
    print(a-b)
elif d == "*":
    print(a*b)
elif d == "/":
    print(a/b)
'''
#Task 3: Even/Odd Check
'''
a = int(input("enter a number: "))

def indenteficationEvenOrOdd(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

indenteficationEvenOrOdd(a)
'''

# Task 4: Basic level
'''
health = int(input("enter a number: "))
def is_alive(health):
    if health <= 0:
        return False
    else:
        return True
'''
# Task 5: Birthday
'''
number_of_month = int(input("Enter the number of the month: "))
def season_events(number_of_month):
    name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    words = {"winter":"White snow fell outside the window","spring":"Birds sang beautiful songs", "summer":"The sun shone brighter than ever", "autumn":"The harvest was incredible"}

    if number_of_month <1 or number_of_month >12:
        print("You need to enter the real number of the month")
    current_month = name[number_of_month - 1]

    if number_of_month in [12, 1, 2]:
        print(f"You were born in {current_month}. {words['winter']}")
    elif number_of_month in [3, 4, 5]:
        print(f"You were born in {current_month}. {words['spring']}")
    elif number_of_month in [6, 7, 8]:
        print(f"You were born in {current_month}. {words['summer']}")
    elif number_of_month in [9, 10, 11]:
        print(f"You were born in {current_month}. {words['autumn']}")

season_events(number_of_month)
'''

'''Task 1 
Given a string containing Russian text. Find the number of words beginning with the letter "e". 
'''
'''

words = input("Enter your word ")

words_list = words.split()

count = 0 

for i in words_list:
    if i.lower().startswith('е'):
        count += 1

print("Количество слов на букву 'е':", count)
'''

'''
Task 2 
In the string, replace all colons (:) with a percent sign (%). Count the number of replacements


words = input("Enter your word: ")
new_word = ''


count = 0 

for i in range(len(words)):
    print(words[i])
    if words[i] != ':':
        new_word += words[i]
    else:
        new_word += '%'
        count += 1

print("Количество замен :", count)
print(new_word)

'''
'''
Task 3 
Delete the dot (.) character in the string and count the number of characters removed.

words = input("Enter your word: ")
new_word = ''


count = 0 

for i in range(len(words)):
    if words[i] != '.':
        new_word += words[i]
    else:
        count += 1

print("Количество замен :", count)
print(new_word)
'''

'''Task 4 
In the string, replace the letter (a) with the letter (o). Count the number of replacements. Count how many characters are in a string. 


words = input("Enter your word: ")
new_word = ''


count = 0 

for i in range(len(words)):
    if words[i] == 'a':
        new_word += "o"
        count += 1
    elif words[i] == "o":
        new_word += "a"
        count += 1
    else:
        new_word += words[i]

print("Количество замен :", count)
print(new_word)
'''
'''Task 5 
Change all uppercase letters to lowercase in a string. 

words = input("Enter your word: ")
new_word = ''


count = 0 

for i in range(len(words)):
    if words[i] == 'a':
        new_word += "o"
        count += 1
    elif words[i] == "o":
        new_word += "a"
        count += 1
    else:
        new_word += words[i]

print("Количество замен :", count)
print(new_word)
'''
'''
Task 6 
Delete all the letters "a" in the string and count the number of characters removed. 

words = input("Enter your word: ")
new_word = ''


count = 0 

for i in range(len(words)):
    if words[i] == 'a':
        count += 1
    else:
        new_word += words[i]

print("Количество замен :", count)
print(new_word)
'''
'''
Task 7 
Given a line. Convert it by replacing with asterisks all the letters "n" that occur among the first n/2 characters. Here n is the length of the string. 

word = input("Enter your word: ")
count = len(word)
result = ''

for i in range(count):
    if i << count//2 and word[i] == 'n':
        result += "*"
    else: 
        result += word[i]

print(result)
'''
'''
Task 8 
Given a string that ends with a dot. Count how many words are in a line. 

text = input("Enter the string: ")

words_list = text.split()

count = len(words_list)

print("Number of words:", count)
'''
'''
Task 9 
Determine how many times the given word occurs in the text. 

target_word = input("Enter your favourite word: ").strip()

sentence = input("Enter your sentence: ")

clean_sentence = sentence.replace('.', '').replace(',', '')

words_list = clean_sentence.split()

count = 0
for word in words_list:
    if word == target_word:
        count += 1

print("Count:", count)
'''
'''Task 10 
The sentence string is given in English. Convert the string so that each word starts with a capital letter. 
'''

'''Task 11 
Given a line. Count the longest sequence of consecutive letters "n". Convert it by replacing all exclamation points with dots. 
'''

'''Task 12 
Given a line. Print all words ending with the letter "I". 
'''

'''Task 13 
Given a string of characters, among which there is one opening and one closing brackets. Display all the characters inside those brackets. 
'''

'''Task 14 
Given a line. Print all words that start with the letter "a" and words that end with the letter "i". 
'''

'''Task 15 
Given a line of text. Count the number of "t"s in the string. 
'''