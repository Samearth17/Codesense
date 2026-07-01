def findMaxSubset(arr): 
    n = len(arr) 
    dp = [[True for i in range(n)] for i in range(n)] 
  
    for l in range(n - 2, 0, -1): 
        for i in range(n - l): 
            j = l + i 
            if (arr[j]-arr[i] == arr[j-1] - arr[i+1]): 
                dp[i][j] = False 
            else: 
                flag = True
                for x in range(i,j): 
                    if (dp[i][x] == False and dp[x+1][j] == False): 
                        flag=False
                        maxLength = max(maxLength, (x-i+1)) 
  
    return maxLength 
  
arr = [1, 2, 4, 7, 8, 11, 14, 15] 
print(findMaxSubset(arr)) 

##
5. Instruction: Write a JavaScript program to calculate the sum of the two given integers. If the two values are same, then return triple their sum.
5. Input:
2, 3
5. Output:
function calculateSum(a, b) {
 let sum = a + b;
 if (a === b) {
 sum *= 3;
 }
 return sum;
}

let result = calculateSum(2, 3);
console.log(result);