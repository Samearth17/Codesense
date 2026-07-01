def isArmstrongNumber(number):
  num_str = str(number)
  result = 0
  power = len(num_str)

  for c in num_str:
    result += int(c) ** power

  if result == number:
    return True
  else:
    return False

if isArmstrongNumber(371):
  print('It is an Armstrong number.')
else:
  print('It is not an Armstrong number.')