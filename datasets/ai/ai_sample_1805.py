def get_consecutive_numbers(numbers):
  consecutive_numbers = []
  for i in range(len(numbers)):
    temp = [numbers[i]]
    for j in range(i+1, len(numbers)):
      if numbers[j] == numbers[i] + 1:
        temp.append(numbers[j])
        i += 1
      else:
        break
    if len(temp) > 1:
      consecutive_numbers.append(temp)

  return consecutive_numbers

if __name__ == '__main__':
    print(get_consecutive_numbers([2, 3, 4, 5, 6, 7, 8, 10, 11, 12]))