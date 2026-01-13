'''At a very famous university, a very famous professor delivered his lectures so
quickly that it was impossible to understand anything. Recently, a student named
Willy decided to conduct a study of the professor's vocabulary. To this end, he
even attended one lecture and recorded everything said on a tape recorder. Then,
by playing the recording back at home at ten times the speed of the tape, Willy was
able to transcribe everything the professor said.
But here's the problem: the professor spoke so quickly that even listening to the
slowed-down recording, it was impossible to tell exactly where he paused between
words. So, Willy has a text consisting of n lowercase English letters he lecture the
professor delivered. Now Willy wants to know how many different words of length
m the professor could have used in his lecture.
Input Data
The first line contains two numbers, n and m (1 ≤ m ≤ n ≤ 100), representing the
lecture length and the word length. The second line contains n English characters
the text of the professor's lecture.
Output Data
In the output print a single number the number of words of length m that the
professor could have used in their lecture.
Input Output
3 1
abc
3
10 3
bbaabbbabb
6
'''

n, m = map(int, input().split())
text = input().strip()

words = set()
for i in range(n - m + 1):
    words.add(text[i:i+m])

print(len(words))