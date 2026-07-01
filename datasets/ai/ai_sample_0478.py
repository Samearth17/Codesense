class MedianCalculator:
    def __init__(self, arr_size):
        self.arr_size = arr_size
        self.arr = []
    
    def calculate_median(self):
        if self.arr_size == 0:
            return 0
        elif self.arr_size == 1:
            return self.arr[0]
        else:
            self.arr.sort()
            if self.arr_size % 2 == 0:
                mid1 = self.arr_size // 2 - 1
                mid2 = self.arr_size // 2
                return (self.arr[mid1] + self.arr[mid2]) / 2
            else:
                return self.arr[self.arr_size // 2]