def separate_odd_even(numbers):
  even = []
  odd = []

  for number in numbers:
    if number % 2 == 0:
      even.append(number)
    else:
      odd.append(number)

  return even, odd

numbers = [2, 4, 7, 8, 11, 9]

even, odd = separate_odd_even(numbers)

print("Even numbers: ", even)
print("Odd numbers: ", odd)