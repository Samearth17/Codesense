def calc_sum(sequence):
 sum = 0
 for num in sequence:
 sum += num
 return sum

def calc_sum_squares(sequence):
 sum = 0
 for num in sequence:
  if num % 2 == 1:
   sum += num * num
 return sum

sequence = [2, 4, 5, 6, 7]
total_sum = calc_sum(sequence)
sum_squares = calc_sum_squares(sequence)

print("Total sum:", total_sum)
print("Sum of squares of odd numbers:", sum_squares)