'''One day, Vasya spent a long time waiting at a bus stop before his bus arrived. To
pass the time, he decided to write down the license plates of passing buses on a
piece of paper, taking a route different from the one he needed. He only wrote
down the main license plate number, ignoring regional affiliation. Ultimately,
Vasya managed to write down N such license plates.
The main part of a license plate number consists of six characters: three letters and
three numbers. A letter begins, then three numbers, and two more letters complete
the entry. Any digit from 0 to 9 can be used as numbers, and only uppercase letters
whose symbols are present in both the English and Russian alphabets can be used
as letters, i.e., only the following characters: A, B, C, E, H, K, M, O, P, T, X, and
Y. For example, "P204BT" is a valid license plate number, while "X182YZ" and
"ABC216" are not.
Your task is to verify the accuracy of Vasya's work. Specifically, it is necessary to
determine which numbers comply with the accepted standard and which do not.
Input Data
The first line of the input contains a single natural number N—the number of
license plates Vasya recorded (N ≤ 50). This is followed by N lines of bus number
entries. Line lengths range from 1 to 300 and contain only characters with ASCII
codes from 33 to 127 (excluding spaces, special characters, and Russian
characters).
Output Data
Print N lines. The i-th line should contain "Yes" if the corresponding i-th license
plate entry is correct and "No" otherwise.
Input Output
5
P204BT
X182YZ
a216bc
A216BC
ABC216
Yes
No
No
Yes
No
'''
allowed_letters = set("ABCEHKMOPTXY")

n = int(input())
for _ in range(n):
    s = input().strip()
    ok = (
        len(s) == 6 and
        s[0] in allowed_letters and
        s[1:4].isdigit() and
        s[4] in allowed_letters and
        s[5] in allowed_letters
    )
    print("Yes" if ok else "No")
