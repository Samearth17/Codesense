def all_palindromic_permutations(myString): 
    if len(myString) == 0: 
        return [''] 
  
    permutationList = [] 
    for i in range(len(myString)): 
        subString = myString[:i] + myString[i+1:] 
        partList = all_palindromic_permutations(subString) 
  
        for permutation in partList: 
            if myString[i] == permutation[0]: 
                permutationList.append(myString[i] + permutation + myString[i])
            else: 
                permutationList.append(permutation + myString[i]) 
   
    return list(set(permutationList))