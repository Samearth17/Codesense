def isInsideCircle(point, center, radius):
    x = point[0] - center[0]
    y = point[1] - center[1]
    distance = (x**2 + y**2)**0.5
    if distance <= radius:
        return True
    return False

point = (2,2)
center = (0, 0)
radius = 5
isInsideCircle = isInsideCircle(point, center, radius)

if isInsideCircle:
    print("Point is inside the circle.")
else:
    print("Point is outside the circle.")