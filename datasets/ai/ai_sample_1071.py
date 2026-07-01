class IteratorExample:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        self.num = self.start
        return self
    
    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            current_num = self.num
            self.num += 1
            return current_num

iterator = IteratorExample(1, 10)
for num in iterator:
    print(num)