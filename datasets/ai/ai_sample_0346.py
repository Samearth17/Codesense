import random

myList = []
for i in range(20):
 myList.append(random.randint(1,20))

print("List of random numbers:", myList)

myList.sort()

largest_num = myList[len(myList)-1]
second_largest_num = myList[len(myList)-2]

print('Largest number:', largest_num)
print('Second-largest number:', second_largest_num)