def mean(lst):
    return sum(lst) / len(lst)

def std_dev(lst):
    avg = mean(lst)
    variance = 0
    for num in lst:
        variance += (num - avg)**2
    variance /= len(lst)
    return variance**0.5

# Driver Code
lst = [5, 7, 10, 8, 6]

print("Mean: ", mean(lst))
print("Standard Deviation: ", std_dev(lst))