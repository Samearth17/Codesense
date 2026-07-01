def mean_median(arr): 
      arr_sum = 0 
      for i in range(len(arr)): 
            arr_sum += arr[i] 
      
      mean = arr_sum/len(arr) 
    
      arr = sorted(arr) 
      if len(arr) % 2 != 0: 
            median = arr[floor(len(arr)/2)] 
      else: 
            median = (arr[len(arr)//2] + arr[len(arr)//2 - 1]) / 2
      
      return mean, median

mean, median = mean_median(arr) 
print("Mean =", mean) 
print("Median =", median)