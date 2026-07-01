# Take three numbers from the user 
Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))
Num3 = int(input("Enter third number: "))

# Find the two smallest numbers 
def two_smallest_nums(Num1, Num2, Num3):
  smallest_num = min(Num1, Num2, Num3)
  mid_num = max( min( Num1, Num2 ), min( Num2, Num3 ) )
  largest_num = max(Num1, Num2, Num3)
  
  # Add the two smallest numbers
  result = smallest_num + mid_num
  return result

sum_result = two_smallest_nums(Num1, Num2, Num3)
print("sum of two smallest numbers = ", sum_result)