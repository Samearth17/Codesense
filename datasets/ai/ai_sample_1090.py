class MyString:
    def __init__(self):
        self.string = ""
 
    def set_string(self, string):
        self.string = string
 
    def get_string(self):
        return self.string
 
    def print_string(self):
        print(self.string)
 
    def get_length(self):
        string_length = len(self.string)
        return string_length