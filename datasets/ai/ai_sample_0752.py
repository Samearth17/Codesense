def select_points_of_distribution(customers, warehouse_location, max_distance):
  # Sort customers by distance from the warehouse
  sorted_customers = sorted(customers, key=lambda c: distance(c, warehouse_location))

  # Keep track of the points of distribution we select
  points_of_distribution = []

  # Initialize variables
  current_customer = 0
  points_covered = 0

  # Iterate until all points are covered
  while points_covered < len(customers):
    # Select the customer with the largest demand
    max_demand_customer = sorted_customers[current_customer]
    points_of_distribution.append(max_demand_customer)

    # Iterate through customers and mark those within the max_distance
    for customer in sorted_customers:
      if distance(max_demand_customer, customer) <= max_distance:
        points_covered += 1

    # Move on to the next customer
    current_customer += 1

  # Return the points of distribution
  return points_of_distribution

def distance(point_1, point_2):
  # Calculate the Euclidean distance between two points
  return math.sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)