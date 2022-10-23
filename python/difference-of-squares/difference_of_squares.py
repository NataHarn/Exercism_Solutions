def square_of_sum(number):
    my_sum = sum(list(range(1, number + 1)))
    return pow(my_sum, 2)


def sum_of_squares(number):
    return sum([pow(num, 2) for num in range(1, number + 1)])


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
