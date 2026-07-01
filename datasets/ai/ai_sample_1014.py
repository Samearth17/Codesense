class FrequencyCounter:
 def __init__(self, string):
  self.string = string
  
 def calculate_frequency(self):
  frequency_dict = {}
  for char in self.string:
   if char in frequency_dict:
    frequency_dict[char] += 1
   else:
    frequency_dict[char] = 1
  return frequency_dict
   
# Use
frequency_counter = FrequencyCounter(string)
frequency_dict = frequency_counter.calculate_frequency()
print(frequency_dict)