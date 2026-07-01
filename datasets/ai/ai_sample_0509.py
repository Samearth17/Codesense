def convert_hexvals_to_decimal(hexvals):
    # Split hexvals on whitespace
    hexvals_list = hexvals.split()
    # Reverse hexvals list
    hexvals_list.reverse()
    decimal_val = 0
    # Loop through hexvals list
    for index, hexval in enumerate(hexvals_list):
        # Multiply hexval by 16^index to calculate decimal value
        decimal_val += int(hexval, 16)*(16**index)
    # Return decimal value
    return decimal_val
    
decimal = convert_hexvals_to_decimal("7a 0d 72")
print(decimal)