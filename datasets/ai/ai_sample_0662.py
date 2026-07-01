def prime_sum(start,end):
    total = 0 
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break 
            else: 
                total += num
    return total

if __name__ == "__main__":
    lower_limit = int(input('Input lower limit: '))
    upper_limit = int(input('Input upper limit: '))
    print(prime_sum(lower_limit, upper_limit))