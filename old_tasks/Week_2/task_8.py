'''
String S1 is called an anagram of string S2 if it is obtained from S2 by rearranging
its characters. Given strings S1 and S2, write a program that checks whether S1 is
an anagram of S2.
Input
The first line contains the string S1, and the second line contains S2. Both lines
consist only of uppercase English letters. The lines are not empty and have a length
of no more than 100,000 characters.
Output
In the output fprint YES if S1 is an anagram of S2, and NO otherwise.
Input Output
ABAA
ABBA
NO
ABBA
BABA
YES
'''
s1 = input()
s2 = input()

# sorted превращает строку в список букв ['A', 'A', 'B', 'B']
if sorted(s1) == sorted(s2):
    print("YES")
else:
    print("NO")