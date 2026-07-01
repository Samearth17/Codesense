def sort_list_by_vowels(list_of_strings):
    vowels = 'aeiouAEIOU'
 
    # Create a list of tuples, with each tuple having a 
    # string and the number of vowels it has
    lst = []
    for i in list_of_strings:
        count = 0
        for j in i:
            if j in vowels:
                count += 1
        lst.append((i, count))
 
    # Sort the list of tuples based on the number of vowels
    lst.sort(key = lambda x: x[1],reverse=True)
 
    # Extract the strings from the list of tuples
    final_list = []
    for i in lst:
        final_list.append(i[0])
 
    return final_list

print(sort_list_by_vowels(["apple", "banana", "kiwi", "strawberry"]))