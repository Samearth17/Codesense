def group_integers(lst):
 evens = []
 odds = []
 for num in lst:
 if (num % 2 == 0):
 evens.append(num)
 else:
 odds.append(num)
 
 return (evens, odds)
 
 lst = [1, 2, 3, 4, 5, 6]
 result = group_integers(lst)
 
 print("Even numbers:", result[0])
 print("Odd numbers:", result[1])