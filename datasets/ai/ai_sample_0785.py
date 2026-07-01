def calculate_standard_deviation(X):
    # Calculate the mean of the list
    mean = 0
    for x in X:
        mean += x
    mean = mean/len(X)

    # Calculate the variance of the list
    variance = 0
    for x in X:
        variance += (x - mean)**2
    variance = variance / len(X)

    # Calculate the standard deviation
    std_dev = variance**0.5

    return std_dev

if __name__ == '__main__': 
    X = [1,2,3,4,5,6]
    print(calculate_standard_deviation(X))