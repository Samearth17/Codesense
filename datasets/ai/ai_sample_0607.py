def add_numbers(numbers):
    """
    Find the sum of a given list of numbers.
    Args:
        numbers: a list of numbers.
    Returns:
        The sum of the numbers.
    """
    sum = 0

    # Iterate over numbers
    for num in numbers:
        # Add number to total
        sum += num

    return sum

total = add_numbers([4, 7, 6, 2])

print(total)