def median_divide_and_conquer(arr):
 if len(arr) == 0:
 return None
 elif len(arr) == 1:
 return arr[0]
 else:
  mid = len(arr) // 2
  l_half = arr[:mid]
  r_half = arr[mid:]
  if len(l_half) % 2 == 0:
   median = (l_half[-1] + l_half[-2]) / 2
  else:
   median = l_half[-1]
  if len(r_half) % 2 == 0:
   median += (r_half[0] + r_half[1]) / 2
  else:
   median += r_half[0]
 return median / 2