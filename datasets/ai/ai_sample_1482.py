def hill_climbing(data):
 # Initialize the best solution to the input solution
 best_solution = data
 best_score = evaluate(data)
 improvement = True

 # While there is an improvement
 while improvement:
 # Get the indices of the two nodes to swap
 a, b = get_swapping_indices(best_solution)

 # Create a new solution by swapping the two nodes
 new_solution = best_solution.copy()
 new_solution[a], new_solution[b] = new_solution[b], new_solution[a]

 # Evaluate the new solution
 new_score = evaluate(new_solution)

 # If it is better than the best solution
 if new_score > best_score:
 # Update the best solution and score
 best_solution = new_solution
 best_score = new_score
 # Otherwise, we cannot improve further
 else:
 improvement = False

 # Return the best solution
 return best_solution

def evaluate(solution):
 # Calculate the total distance travelled
 total_distance = 0

 for i in range(len(solution)):
 total_distance += abs(solution[i] - solution[(i+1) % len(solution)])

 # Return the total distance
 return total_distance

def get_swapping_indices(solution):
 # Choose two random indices
 a = random.randint(0, len(solution) - 1)
 b = random.randint(0, len(solution) - 1)

 # Make sure they are different
 while a == b:
 b = random.randint(0, len(solution) - 1)

 # Return the indices
 return a, b