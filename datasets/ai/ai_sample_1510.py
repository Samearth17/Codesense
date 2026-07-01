import base64
from Crypto.Cipher import AES

secret_key = "YourSecr3tEncrKey"

def encodeAES(text):
Key = base64.b64encode(secret_key.encode("utf-8"))

IV = 16 * '\x00' 

mode = AES.MODE_CBC
encryptor = AES.new(Key, mode, IV=IV)
text = text.encode("utf-8")
ciphertext = encryptor.encrypt(text)

return base64.b64encode(ciphertext).decode("utf-8")