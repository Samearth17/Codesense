def generate_fibonacci(length):
    # Initialize
    n1, n2 = 0, 1

    # Check if length is valid
    if length <= 0:
        print('Invalid length. Positive numbers only.')
    elif length == 1:
        print(n1)
    else:
        print(n1, n2, end=' ')
    
    # Generate sequence
    for i in range(2, length):
        n3 = n1 + n2
        print(n3, end=' ')
        n1 = n2
        n2 = n3

# Show output
generate_fibonacci(6)
# Output: 0 1 1 2 3 5