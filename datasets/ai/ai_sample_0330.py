list = [1, 2, 3, 4, 5, 2, 3, 1, 6, 3]

def findDuplicates(list):
 result = []
 seen = set()
 
 for num in list:
 if num not in seen:
 seen.add(num)
 else:
 result.append(num)
 
 return result

print(findDuplicates(list))