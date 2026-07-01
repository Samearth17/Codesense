class StringCaseModifier:
    def __init__(self, string):
        self.string = string

    def to_upper(self):
        return self.string.upper()

    def to_lower(self):
        return self.string.lower()
    
    def to_title(self):
        return self.string.title()

if __name__ == '__main__':
    test_string = 'Hello World'
    string_modifier = StringCaseModifier(test_string)
    print(string_modifier.to_upper())
    print(string_modifier.to_lower())
    print(string_modifier.to_title())