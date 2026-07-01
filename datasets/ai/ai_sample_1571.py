# Compose a program in Python to find the sum of an array of integers

def array_sum(arr):
  """
  Compute the sum of an array of integers.

  Parameters
  ----------
  arr : array_like
    The array of integers.

  Returns
  -------
  int
    The sum of the array entries.
  """
  sum = 0
  for n in arr:
    sum += n
  return sum