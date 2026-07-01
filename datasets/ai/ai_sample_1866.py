ships = []
permutations = [[]]

def generate_ships(components, index, permutation):
 if index == len(components):
 ships.append(permutation)
 else:
 for i in [0, 1]:
 permutation_copy = permutation.copy()
 permutation_copy.append(i)
 generate_ships(components, index + 1, permutation_copy)

# Initial call
generate_ships(components, 0, [])

print(ships)