def closest_pair(points): 
    min_distance = float('inf')
    n = len(points) 
    for i in range(n-1): 
        for j in range(i+1, n): 
            distance = ((points[i][0] - points[j][0])**2 + 
                        (points[i][1] - points[j][1])**2)**0.5 
            if distance < min_distance: 
                min_distance = distance
                min_pair = (points[i], points[j]) 
  
    return min_distance, min_pair 

points = [(1,1), (3,3), (-2, 4), (-3, -2), (2, 4)] 
print(closest_pair(points))