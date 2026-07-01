def most_frequent_item(myList):
    max_item = myList[0]
    max_count = 1
    for i in range(1, len(myList)):
        count = 1
        for j in range(i+1, len(myList)):
            if(myList[i] == myList[j]):
                count += 1
                if(count > max_count):
                    max_count = count
                    max_item = myList[i]
    
    return (max_item)

myList = [1, 2, 3, 2, 4, 2]
print(most_frequent_item(myList))