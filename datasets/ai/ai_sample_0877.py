import sys

dictionary={}

for line in sys.stdin:
 words_in_line = line.split()
 for word in words_in_line:
 word=word.lower()
 if word in dictionary:
 dictionary[word]+=1
 else:
 dictionary[word]=1

for word in dictionary:
 print(word +":"+ str(dictionary[word]))