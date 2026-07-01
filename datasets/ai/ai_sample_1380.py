def find_closest_pair_of_points(points): 
  min_dist = float("inf") 
  pair=[None, None]
  for i in range(len(points)): 
    for j in range(i + 1, len(points)): 
      dist = dist_between_points(points[i], points[j]) 
      if dist < min_dist: 
        min_dist = dist 
        pair[0], pair[1] = points[i], points[j] 
  return pair 

def dist_between_points(p1, p2): 
  x1, y1 = p1 
  x2, y2 = p2 
  return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)