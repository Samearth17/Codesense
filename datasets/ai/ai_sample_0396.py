# Generate a program in Python to find the maximum element in a given array

def maximum_element(arr):
  """
  Find the maximum element in a given array.

  Parameters
  ----------
  arr : array_like
    The array of integers.

  Returns
  -------
  int
    The maximum value found in the array, or None if the array is empty.
  """
  max_element = None
  for n in arr:
    if max_element is None or n > max_element:
      max_element = n
  return max_element