def calculate_area(shape, *args):
 if shape == 'triangle':
 base= args[0]
 height= args[1]
 return (0.5 * base * height)

 elif shape == 'square':
 side = args[0]
 return (side ** 2)

 elif shape == 'rectangle':
 length = args[0]
 breadth = args[1]
 return (length * breadth)

 elif shape == 'circle':
 radius = args[0]
 return (3.142 * radius * radius)

else:
 return "Incorrect shape"