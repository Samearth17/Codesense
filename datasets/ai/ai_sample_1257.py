def get_coins(coins, change):
	min_coins = change
	if change in coins:
		return [change]

	for i in [c for c in coins if c <= change]:
		num_coins = 1 + get_coins(coins, change-i)
		if len(num_coins) < min_coins:
			min_coins = num_coins
	return min_coins

# Test 
coins = [1, 6, 10]
change = 8
print(get_coins(coins, change)) # [1, 6, 1]