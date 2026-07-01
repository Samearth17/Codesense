#Greedy algorithm to solve scheduling problem

#Optimal order
order = []

#Sort jobs according to end time
pro_idx = [i[0] for i in sorted(enumerate(End), key=lambda x:x[1])]

#Calculate result
totalProfit = 0
curr_time = 0
for i in range(len(pro_idx)):
    #Choose job in optimal order
    idx = pro_idx[i]
 
    #Check if job starts later than current time
    start = Start[idx]
    if start >= curr_time:
        order.append(idx + 1)
        curr_time = End[idx]
        totalProfit += Profit[idx]
 
#Print results
print("Optimal order:", order)
print("Maximum profit:", totalProfit)