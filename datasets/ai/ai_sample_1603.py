def permutations(string): 
    if string == "": 
        return [''] 
          
    prev_list = permutations(string[1:]) 
    next_list = [] 
    char = string[0] 
    for word in prev_list: 
        for j in range(len(word) + 1): 
            next_list.append(word[:j] + char + word[j:]) 
    return next_list 

string = "abc"
perm_list = permutations(string) 
print (perm_list)