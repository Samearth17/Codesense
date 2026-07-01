import random 
  
def heads_tails(): 
    heads = 0
    tails = 0
    res = ["H", "T"]
    tosses = int(input("Number of tosses: "))
    sequence = ""
    for i in range(tosses): 
        if random.choice(res) == "H": 
            heads += 1
            sequence += "H"
        else: 
            tails += 1
            sequence += "T"
    print("Heads: ", heads) 
    print("Tails: ", tails)
    print("Sequence:", sequence)

heads_tails()