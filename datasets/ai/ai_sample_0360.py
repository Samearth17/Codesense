def generateHammingCode(bitString):
    # Get length of the input bit string
    n = len(bitString) 
  
    # Calculate the number of parity bits
    m = 0
    while 2**m < n + m + 1: 
        m+= 1
  
    # Initialize 2 empty lists to store parity and encoded bits
    parityBits = [] 
    encodedList = [] 
  
    # Calculate parity bits
    for i in range(m): 
        k = 2**i 
        parityBits.append(calculateParityBit(bitString, k)) 
  
    # Generate hamming code
    j = 0
    for i in range (1, n + m + 1): 
        if i == 2**j: 
            encodedList.append(parityBits[j])
            j += 1
        else :
            encodedList.append(int(bitString[i - j - 1]))
          
    return encodedList
  
def calculateParityBit(bitString, k): 
    counter = 0
    for i in range(len(bitString)): 
        if i & k == k :
            counter += int(bitString[i]) 
    if counter % 2 == 0: 
        return '0'
    else: 
        return '1'