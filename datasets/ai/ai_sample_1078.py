def findLengthOfLCIS(A):
    n = len(A)
    if n == 0:
        return 0
    ans = 1
    prev = A[0]
    curr_len = 1
    for i in range(1, n):
        if A[i] > prev:
            curr_len += 1
        else:
            ans = max(ans, curr_len)
            curr_len = 1
        prev = A[i]
    return max(ans, curr_len)

if __name__ == '__main__':
    A = [1, 9, 3, 10, 4, 20, 2]
    print("Length of LCIS is", findLengthOfLCIS(A))