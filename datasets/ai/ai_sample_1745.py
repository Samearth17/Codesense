def encode_message(message, a, b):
    encoded_message = ""
    for char in message:
        # encode each character
        x = (ord(char) - 97) * a + b
        # wrap around if x is greater than 26
        x = x % 26
        # convert back to character
        encoded_message += chr(x + 97)
    return encoded_message

# Main
if __name__ == "__main__":
    message = "Hello world"
    a = 3  # a and b must be relatively prime
    b = 5
    print(encode_message(message, a, b))  # Khoor zruog