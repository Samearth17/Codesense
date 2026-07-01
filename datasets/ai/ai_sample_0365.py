def jobScheduling(jobs):
    n = len(jobs) 
    
    jobs = sorted(jobs, key = lambda x: x[1]) 
   
    table = [0 for i in range(n)] 
    table[0] = jobs[0][2] 
  
    for i in range(1, n): 
  
        inclProf = jobs[i][2] 
        l = binarySearch(jobs, i) 
        if (l != -1):
            inclProf += table[l] 
  
        table[i] = max(inclProf, table[i-1]) 
  
    return table[n-1]