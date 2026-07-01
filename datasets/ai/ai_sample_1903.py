import base64
from Crypto.Cipher import AES

def encrypt(key, text):
 cipher = AES.new(key, AES.MODE_EAX)
 nonce = cipher.nonce
 ciphertext, tag = cipher.encrypt_and_digest(text.encode('utf-8'))
 return (nonce, tag, ciphertext)

key = b'Sixteen byte key'
text = "hello world"

nonce, tag, ciphertext = encrypt(key, text)

encoded_nonce = base64.b64encode(nonce)
encoded_tag = base64.b64encode(tag)
encoded_ciphertext = base64.b64encode(ciphertext)

print("Encrypted Text:", encoded_nonce, encoded_tag, encoded_ciphertext)