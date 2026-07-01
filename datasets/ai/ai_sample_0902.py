def kClosestValues(arr, x, k):
    closestPrimes = []
    diff = float("inf")
    for num in arr:
        currentDiff = abs(num - x)
        if currentDiff <= diff:
            if currentDiff < diff:
                closestPrimes = []
            closestPrimes.append(num)
            diff = currentDiff
    if closestPrimes[0] > x:
        closestPrimes.sort()
    else:
        closestPrimes.sort(reverse=True)
    return closestPrimes[:k]