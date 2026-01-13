'''
A cyclic shift of a string s is the string for some k,
where |s| is the length of s. A substring of s is the string for some i
and j. You are given two strings a and b. Print the number of substrings of a that
are cyclic shifts of b.
Input Data
The first line of the input contains the string a (1 ≤ |a| ≤ 1000). The second line of
the input filcontains the string b (1 ≤ |b| ≤ min(100,|a|)). Both strings consist only
of English alphabetic characters and digits.
Output Data
Print an integer—the answer to the problem
Input Output
abcabc
abc
4
abcabc
acb
0
aaaaaaa
aa
6
aAaa8aaAa
aAa
4'''

a = input()
b = input()

bb = b + b

shifts = set()
len_b = len(b)

for i in range(len_b):
    shifts.add(bb[i:i+len_b])

count = 0 

for i in range(len(a) - len_b + 1):
    if a[i:i + len_b] in shifts:
        count +=1

print(shifts)
print(count)