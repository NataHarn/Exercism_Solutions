def equilateral(sides):
    return triangle_check(sides) and len(set(sides)) == 1

def isosceles(sides):
    return triangle_check(sides) and len(set(sides)) <= 2

def scalene(sides):
    return triangle_check(sides) and len(set(sides)) == 3

def triangle_check(sides):
    sides_sum = sum(sides)
    if sides_sum == 0:
        return False
    for side in sides:
        if sides_sum - side < side:
            return False
    return True
