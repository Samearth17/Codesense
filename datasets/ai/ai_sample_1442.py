def get_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fibonacci(n-1) + get_fibonacci(n-2)

def get_fibonacci_series(start, end):
    series = []
    for i in range(start, end+1):
        series.append(get_fibonacci(i))
    return series

if __name__ == '__main__':
    start = 5
    end = 10
    result = get_fibonacci_series(start, end)
    print(result)