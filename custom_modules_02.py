pi = 3.14159

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius

def area(radius:float) -> float:
    """
    Takes the radius of a circle and returns the area
    """
    return pi * (radius ** 2)