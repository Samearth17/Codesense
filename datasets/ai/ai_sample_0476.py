def sort_list(list):
   for i in range(len(list)-1):          # loop over index i from 0 to n-2
       small = i                         # set minimum index to i
       for j in range(i + 1, len(list)): # loop over index j from i+1 to n-1
           if list[j] < list[small]:      # compare list[j] with list[small]
               small = j                  # update minimum index
       list[i], list[small] = list[small], list[i]  # swap list[i] and list[small]
   return list


# Main program
list = [ 3, 8, 4, 6, 2, 9, 7]
print ("Original list:", list)
sort_list(list)
print ("Sorted list:", list)