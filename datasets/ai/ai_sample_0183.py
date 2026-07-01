class PrimeNumber:
    def __init__(self, num):
        self.num = num

    def is_prime(self):
        for i in range(2, self.num):
            if(self.num % i == 0):
                return False
        return True

num = 10
obj = PrimeNumber(num)

if obj.is_prime():
    print("Number is Prime")
else:
    print("Number is Composite")