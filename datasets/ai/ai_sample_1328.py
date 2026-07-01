# Define a function to print an int in binary format
def print_binary(n):
    if n < 0:
        print("Negative numbers are not supported.")
        return
    if n == 0:
        print("0b0")
    else:
        result = []
        while n > 0:
            result.append(n % 2)
            n = n // 2

        result.reverse()
        print("0b" + "".join(str(x) for x in result))
        
# Define a function to count the number of bits set
def bits_set(n):
    if n == 0:
        return 0
    else:
        result = 0
        while n > 0:
            result += n % 2
            n = n // 2
        return result

# Read an int
n = int(input("Enter an int: "))

# Print the int in binary format
print_binary(n)

# Print the number of bits set to 1
bits_count = bits_set(n)
print("Number of bits set:", bits_count)