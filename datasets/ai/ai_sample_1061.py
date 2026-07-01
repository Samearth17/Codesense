class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.fib = []
    
    def generate_list(self):
        if self.n <= 0:
            print('Invalid input.')
        elif self.n == 1:
            self.fib = [0]
        else:
            self.fib = [0,1]
            for i in range(2,self.n):
                self.fib.append(self.fib[i-2] + self.fib[i-1])
        return self.fib