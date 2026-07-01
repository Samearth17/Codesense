def calculate_area(n):
    """
    Calculates the area of an n-sided regular polygon
    """
    # Calculate the area of the n-sided regular polygon
    side_length = 1
    area = (n * side_length**2) / (4 * math.tan(math.pi / n))
    return round(area, 2)

# Get the number of sides as an input
n = int(input("Enter the number of sides"))

# Calculate the area and print it
area = calculate_area(n)
print("The area of the regular polygon is", area)