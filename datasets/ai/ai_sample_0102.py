class Matrix: 
    def __init__(self, m, n, lst): 
        self.m = m             
        self.n = n             
        self.mat = [] 
  
        c = 0
        for i in range(self.m): 
            a =[] 
            for j in range(self.n): 
                    a.append(lst[c]) 
                    c += 1
            self.mat.append(a) 
  
    def __str__(self): 
        output = ""
        for i in self.mat: 
            for j in i: 
                output += str(j) + " "
            output += '\n'
        return output 
  
    def add(self, mat2): 
        for i in range(self.m): 
            for j in range(self.n): 
                self.mat[i][j] += mat2.mat[i][j] 
  
    def sub(self, mat2): 
        for i in range(self.m): 
            for j in range(self.n): 
                self.mat[i][j] -= mat2.mat[i][j]
    
    def mul(self, mat2): 
        result = [] 
        for i in range(self.m): 
            a =[] 
            for j in range(mat2.n): 
                s = 0
                for k in range(self.n): 
                    s += self.mat[i][k] * mat2.mat[k][j] 
                a.append(s) 
            result.append(a) 
        self.mat = result 
        self.m = len(result) 
        self.n = len(result[0]) 
  
    def transpose(self):
        result = [[self.mat[j][i] for j in range(len(self.mat))] for i in range(len(self.mat[0]))]
        self.mat = result 
        self.m = len(result) 
        self.n = len(result[0])