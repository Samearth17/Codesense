"""
Providing a Python program that resizes an array of integers in place
"""
def resize_array(arr, new_size):
    # base case
    if len(arr) == new_size:
        return

    # add elements to increase the size
    if len(arr) < new_size:
        for _ in range(new_size - len(arr)):
            arr.append(0)

    # delete elements to decrease the size    
    elif len(arr) > new_size:
        for _ in range(len(arr) - new_size):
            arr.remove(arr[-1])

if __name__ == '__main__':
    arr = [10, 20, 30, 40]
    new_size = 6
    resize_array(arr, new_size)
    print(arr)