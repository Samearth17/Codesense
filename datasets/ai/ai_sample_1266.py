class Statistics:
    def __init__(self):
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def mean(self):
        return sum(self.scores) / len(self.scores)

    def variance(self):
        mean = self.mean() 
        return sum((x - mean) ** 2 for x in self.scores) / len(self.scores)

    def median(self):
        self.scores.sort()
        mid = len(self.scores) // 2
        if len(self.scores) % 2 == 0:
            median = (self.scores[mid - 1] + self.scores[mid]) / 2
        else:
            median = self.scores[mid]
        return median

    def mode(self):
        mode = []
        nums = {} 
        for num in self.scores: 
            if num in nums: 
                nums[num] += 1
            else: 
                nums[num] = 1
  
        max_freq = max(nums.values()) 
  
        for num in nums: 
            if nums[num] == max_freq: 
                mode.append(num) 

        return mode