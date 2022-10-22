# get the number of grains in each square
def square(number):
    if number < 1 or number > 64:
        # raise error when not inputting values from 1 - 64
        raise ValueError("square must be between 1 and 64")
    return pow(2, number-1)

# get total number of grains
def total():
    total = 0
    for number in range(1, 65):
        total += square(number)
    return total
