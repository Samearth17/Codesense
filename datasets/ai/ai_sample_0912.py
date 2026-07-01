rectA_min = (2, 6)
rectA_max = (4, 2)

rectB_min = (3, 5)
rectB_max = (6, 3)

def check_overlap(rectA, rectB):
  overlap_x = min(rectA_max[0], rectB_max[0]) - max(rectA_min[0], rectB_min[0])
  overlap_y = min(rectA_max[1], rectB_max[1]) - max(rectA_min[1], rectB_min[1])
 
  if overlap_x>0 and overlap_y>0:
    overlap_area = overlap_x * overlap_y
    return overlap_area
  else:
    return 0