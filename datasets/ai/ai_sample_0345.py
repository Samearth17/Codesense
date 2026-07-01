a, b = 0, 1
for i in range(10):
  print(a)
  a, b = b, a + b

# Output:
0
1
1
2
3
5
8
13
21
34