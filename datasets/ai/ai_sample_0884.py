def permutation(str):
    if len(str) == 0:
        return []
    if len(str) == 1:
        return [str]
    l = [] 
    for i in range(len(str)):
       m = str[i] 
       remLst = permutation(str[:i] + str[i+1:])
       for p in remLst:
           l.append(m + p)
    return l

string = 'ABC'
l = permutation(string)
for s in l:
    print(s)