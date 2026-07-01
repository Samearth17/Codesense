def shortest_substring(s1, s2): 
      
    s1_len = len(s1) 
    s2_len = len(s2) 

    res_str = ""
    res_len = s1_len + s2_len 
      
    for i in range(s1_len): 
        for j in range(s2_len): 
              
            # Initializing starting and ending indexes 
            # of current substring 
            x = i 
            y = j 
              
            # Initializing substring 
            tmp_str = "" 
          
            # flag to keep track of the order in which two  
            # characters have been found 
            flag = 0
          
            while (x < s1_len and y < s2_len): 
                if s1[x] != s2[y]: 
                    break
                  
                # tmp_str stores the current substring 
                if flag == 0: 
                    tmp_str += s1[x] 
                else: 
                    tmp_str += s2[y]; 
          
                x += 1
                y += 1
                  
                flag = 1 - flag 
          
            # Updating minimum length substring 
            if (len(tmp_str) < res_len): 
                res_len = len(tmp_str) 
                res_str = tmp_str 
  
    return res_str 

result = shortest_substring("abbcd", "accde")
print(result)