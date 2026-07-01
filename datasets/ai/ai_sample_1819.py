import random
def random_walk_algo(steps):
    x, y = 0, 0
    for _ in range(steps):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x,y)

def rmsd(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

steps = 200
point1 = random_walk_algo(steps)
point2 = random_walk_algo(steps)
rmsd_res = rmsd(point1, point2)
print('Root mean squared displacement = {}'.format(rmsd_res))