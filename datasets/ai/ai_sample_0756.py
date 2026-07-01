def is_palindrome(num):
  rev = 0
  tmp = num
  
  while tmp > 0:
    rev = rev * 10
    rev = rev + (tmp % 10)
    tmp = tmp // 10

  return num == rev
  
num = 12321
if (is_palindrome(num)):
  print("Number is a palindrome")
else:
  print("Number is not a palindrome")