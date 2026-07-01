def calculate_mean_median_mode(arr):
 mean = 0
 sum = 0
 mode = None
 for i in range(len(arr)):
 sum += arr[i]
 mean = sum / len(arr)
 arr.sort()
 if len(arr) % 2 == 0:
 median = (arr[int(len(arr) / 2)] + arr[int(len(arr) / 2) - 1]) / 2
 else:
 median = arr[int(len(arr) / 2)]
 count = 0
 max_count = 0
 for i in range(len(arr)):
 current_count = 0
 for j in range(len(arr)):
 if arr[i] == arr[j]:
 current_count += 1
 if current_count > max_count:
 max_count = current_count
 mode = arr[i]
 return [mean, median, mode]