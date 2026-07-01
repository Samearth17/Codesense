def knapsack(items, maxWeight):
    maxValue = 0
    knapsackItems = []
    n = len(items)

    for i in range(1 << n):
        curWeight = 0
        curValue = 0
        for j in range(n):
            if (i & (1 << j)) != 0:
                curWeight += items[j]["weight"]
                curValue += items[j]["value"]
        if curWeight <= maxWeight and curValue > maxValue:
            maxValue = curValue
            knapsackItems = []
            for j in range(n):
                if (i & (1 << j)) != 0:
                    knapsackItems.append(items[j]["name"])
    return knapsackItems

items = [{"name": "pencil", "weight": 5, "value": 10},
         {"name": "eraser", "weight": 3, "value": 5},
         {"name": "book", "weight": 8, "value": 15},
         {"name": "notebook", "weight": 2, "value": 3}] 
maxWeight = 8

knapsackItems = knapsack(items, maxWeight)
print(knapsackItems)