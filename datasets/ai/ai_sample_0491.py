def sphere_surfacearea(radius):
    """
    Calculates surface area of a sphere given its radius
    :param radius: Radius of sphere
    :return: Surface area of a sphere
    """
    return 4 * math.pi * (radius ** 2)

def sphere_volume(radius):
    """
    Calculates the volume of a sphere given its radius
    :param radius: Radius of sphere
    :return: Volume of a sphere
    """
    return (4 / 3) * math.pi * (radius ** 3)