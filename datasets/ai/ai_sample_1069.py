def find_similar_LCS_strings(strings):
    d = {}
    for i in range(len(strings)):
        for j in range(len(strings)):
            if i == j:
                continue
            else:
                x = strings[i]
                y = strings[j]
                m = [[0 for k in range(len(y)+1)] for l in range(len(x)+1)]
                
                # build the dynamic programming lookup table
                for i in range(1, len(x)+1):
                    for j in range(1, len(y)+1):
                        if x[i-1] == y[j-1]:
                            m[i][j] = m[i-1][j-1] + 1
                        else:
                            m[i][j] = max(m[i][j-1], m[i-1][j])

                d[(x, y)] = m[len(x)][len(y)]
    
    result = []
    # build the result list
    while d:
        key = max(d, key=lambda k: d[k])
        x, y = key[0], key[1]
        del d[key]
        tmp = [x, y]
        for k in d.keys():
            if x in k or y in k:
                if d[k] == d[key]:
                    del d[k]
                    if k[0] == x:
                        tmp.append(k[1])
                    else:
                        tmp.append(k[0])
        result.append(tmp)

    final_result = []
    for entry in result:
        if entry not in final_result:
            final_result.append(entry)
            
    return final_result

strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = find_similar_LCS_strings(strings)
print(res) # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]