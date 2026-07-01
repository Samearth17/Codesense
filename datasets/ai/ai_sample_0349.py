from collections import Counter

string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
words = string.split()

cnt = Counter()
for word in words:
  cnt[word] += 1

word, count = cnt.most_common(1)[0]

print(f'Word with highest frequency is "{word}" occurring {count} times.')

# Output
Word with highest frequency is "dolor" occurring 1 times.