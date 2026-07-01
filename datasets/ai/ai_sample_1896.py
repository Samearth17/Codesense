list_nums = [10, 2, 3, 8, 7, 6, 5, 9, 4, 1];

# find the mid point of the list
list_len = len(list_nums);
mid = list_len//2

# split list into two sublists
list_1 = list_nums[:mid]
list_2 = list_nums[mid:]

# sum up all the numbers in each sublist
sum_1 = 0
sum_2 = 0

for num in list_1:
 sum_1 += num

for num in list_2:
 sum_2 += num

# check if the sum of each of the two sublists is roughly equal
if abs(sum_1 - sum_2) < 10:
 print(f'The lists {list_1} and {list_2} have a sum difference of {abs(sum_1 - sum_2)}')

else:
 print('The two sublists are not equal in sum')