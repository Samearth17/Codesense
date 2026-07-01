# Python program to remove vowels from a string

def remove_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    output_string = ""
    for char in string:
        if char not in vowels:
            output_string += char
    return output_string

if __name__ == "__main__":
    string = "Hello World!"
    print("Original String:", string)
    string = remove_vowels(string)
    print("String without Vowels:", string)