def calculate_mode(sequence):
 counts = {}
 for num in sequence:
 if num in counts:
 counts[num] += 1
 else:
 counts[num] = 1
 
 max_count = 0
 mode_num = 0
 for key, value in counts.items():
 if value > max_count:
 max_count = value
 mode_num = key
 
 return mode_num