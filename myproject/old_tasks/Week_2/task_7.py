'''Shopping List Analysis (Collections)
A store recorded a list of items purchased by customers during the day.
Each purchase is represented by a string (the item name).
You need to:
1. Count how many times each item was purchased
2. Find the most frequently purchased item
3. Output all items that were purchased exactly once
4. Sort the items by descending purchase count
Input
apple banana apple orange banana apple milk
Output
Purchase frequency:
apple: 3
banana: 2
orange: 1
milk: 1
Most popular item: apple
Purchased once: orange milk
Sorted by frequency:
apple 3
banana 2
orange 1
milk 1
'''

from collections import Counter

items = input().split()
freq = Counter(items)

print("Purchase frequency:")
for item, count in freq.items():
    print(f"{item}: {count}")

most_common = freq.most_common(1)[0][0]
print("\nMost popular item:", most_common)

once = [item for item, count in freq.items() if count == 1]
print("\nPurchased once:", " ".join(once))

print("\nSorted by frequency:")
for item, count in freq.most_common():
    print(item, count)