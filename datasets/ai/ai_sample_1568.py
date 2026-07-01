# encode
import base64

string = "Hello World!"

#Encode to Base64
encodedBytes = base64.b64encode(string.encode("utf-8"))
encodedString = str(encodedBytes, "utf-8")

print(encodedString)

# decode
encodedString = 'SGVsbG8gV29ybGQh'

#Decode from Base64
decodedBytes = base64.b64decode(encodedString)
decodedString = str(decodedBytes, "utf-8")

print(decodedString)