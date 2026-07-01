class ReverseString():
    
    def __init__(self, string):
        self.string = string
    
    def reverse(self):
        splittedString = self.string.split(' ')
        reversedString = []
        for word in splittedString:
            reversedString.insert(0, word)
        reversedString = ' '.join(reversedString)
        return reversedString
        
r = ReverseString(string)
print(r.reverse())