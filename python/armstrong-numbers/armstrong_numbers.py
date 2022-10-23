def is_armstrong_number(number):
    number = str(number)
    n = len(number)
    num_sum = 0
    for digit in number:
        num_sum += pow(int(digit), n)
    return int(number) == num_sum