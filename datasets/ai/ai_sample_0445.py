def linear_search(x, n):
    found = False
    for i in range(len(x)):
        if x[i] == n:
            found = True
            break

    if found == True:
        print('Element', n, 'found at position', i)
    else:
        print('Element', n, 'not found')

x = [1, 5, 8, 3]
n = 8

linear_search(x, n)