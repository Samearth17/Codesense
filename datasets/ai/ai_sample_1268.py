def separate_list(numbers):
    prime_nums = []
    composite_nums = []
    odd_even_nums = []

    for num in numbers:
        if num == 1:
            prime_nums.append(num)
        elif all([num % i != 0 for i in range(2,num)]):
            prime_nums.append(num)
        else:
            composite_nums.append(num)
        if num % 2 == 0:
            odd_even_nums.append(num)
        else: 
            odd_even_nums.append(num)
    return prime_nums, composite_nums, odd_even_nums