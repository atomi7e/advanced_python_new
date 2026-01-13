import string
from collections import Counter

try:
    with open("text.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        
    num_lines = len(lines)
    

    full_text = "".join(lines).lower()
    
    for char in string.punctuation:
        full_text = full_text.replace(char, "")
        
    words = full_text.split()
    
    num_words = len(words)
    
    word_freq = Counter(words)
    
    with open("analysis.txt", "w", encoding="utf-8") as out_file:
        out_file.write(f"Total lines: {num_lines}\n")
        out_file.write(f"Total words: {num_words}\n")
        out_file.write("Word frequency:\n")
        
        for word, count in word_freq.most_common():
            out_file.write(f"{word}: {count}\n")
            
    print("Done! Results saved in analysis.txt")

except FileNotFoundError:
    print("Error: File text.txt not found. Create it first.")