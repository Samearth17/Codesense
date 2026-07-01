from Cryptodome.Cipher import AES

def encrypt(message, key):
    # Block size should match the chosen AES mode
    block_size = 16
    padding_length = block_size - len(message) % block_size

    # Padding must always be present per the AES spec
    if padding_length:
        padded_message = message + (chr(padding_length) * padding_length)
    else:
        padded_message = message

    # CBC Mode always works with 16 byte blocks
    iv = b'\x16\x87r\xb9\x1b\x8bho\x04u\x16\xdb\xbc\x98\x87\xb7Y\xc0'

    # Create cipher and encrypt data
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_message = cipher.encrypt(padded_message.encode('utf-8'))

    return encrypted_message

key = b'#1\x84\xdc\x06\x0c\x12\xe8\x0c\xd7 \x9d\x03\xd4*\xdd[\x85'

encrypted_message = encrypt("My Secret Message",key)

print(encrypted_message)
# b"B\xf5{5<\xec~\xf9\xc9\x8f_3\x04\x95\x15'\x90\xd2\\\xfc\xd9\x03\xdc\x1dr\x1b"