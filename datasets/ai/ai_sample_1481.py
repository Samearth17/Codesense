class MeanMedianModeCalculator:
    
    # Function to calculate the mean  
    def calculate_mean(self, numbers):
        return sum(numbers) / len(numbers)
    
    # Function to calculate the median  
    def calculate_median(self, numbers):
        numbers.sort()
        mid_point = int(len(numbers) / 2)
        if len(numbers) % 2 == 0:
            return (numbers[mid_point - 1] + numbers[mid_point]) / 2
        else: 
            return numbers[mid_point]
            
    # Function to calculate the mode 
    def calculate_mode(self, numbers):
        max_count = 0
        max_num = 0
        count_dictionary = {}
        
        for number in numbers:
            if number in count_dictionary.keys():
                count_dictionary[number] += 1
            else:
                count_dictionary[number] = 1
                
            if count_dictionary[number] > max_count:
                max_count = count_dictionary[number]
                max_num = number
                
        return max_num