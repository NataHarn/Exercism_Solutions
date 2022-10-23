def sum_of_multiples(limit, multiples):
    my_num = set()
    for number in multiples:
        if number == 0:
            number_limit = 1
        elif limit % number == 0:
            number_limit = limit / number -1
        else:
            number_limit = limit // number
        for n in range(1, int(number_limit) + 1):
            my_num.add(number * n)
    return sum(my_num)
