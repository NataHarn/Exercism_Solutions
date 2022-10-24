def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        divisors = {1}
        count = 2
        max_r = number
        while (count < max_r):
            if number % count == 0:
                divisors.add(count)
                divisors.add(number / count)
                max_r = number / count
            count += 1
        if len(divisors) == 1:
            divisors.remove(1)
    sum_div = int(sum(divisors))
    if sum_div == number:
        return 'perfect'
    elif sum_div > number:
        return 'abundant'
    return 'deficient'
    