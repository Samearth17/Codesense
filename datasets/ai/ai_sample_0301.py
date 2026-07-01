# Non-recursive algorithm
num_1 = int(input('Please enter the first number: '))
num_2 = int(input('Please enter the second number: '))

def prod_non_recursive(num_1, num_2):
    product = 1
    while num_2 > 0:
        product = product * num_1
        num_2 = num_2 - 1
    return product

product_non_recursive = prod_non_recursive(num_1, num_2)
print('The product of {} and {} is {}.'.format(num_1, num_2, product_non_recursive))


# Recursive algorithm
def prod_recursive(num_1, num_2):
    if num_2 == 0:
        return 1
    else:
        return num_1 * prod_recursive(num_1, num_2 - 1)

product_recursive = prod_recursive(num_1, num_2)
print('The product of {} and {} is {}.'.format(num_1, num_2, product_recursive))