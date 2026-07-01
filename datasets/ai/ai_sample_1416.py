def compress(string):
    if string == '' or not string:
        return string
    compressed_str = []
    i = 0
    j = 0
    while i < len(string):
        while j < len(string) and string[j] == string[i]:
            j = j + 1
        compressed_str.append([string[i], str(j-i)])
        i = j
    return compressed_str

def decompress(compressed_str):
    decompressed_str = ""
    for i in compressed_str:
        decompressed_str+=i[0]*int(i[1])
    return decompressed_str