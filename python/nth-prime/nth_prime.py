def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    counter, numerator = 0, 1
    while counter < number:
        numerator += 1
        prime = True
        for i in range(1, int(numerator**(1/2))+1):
            if i == 1:
                continue
            if numerator % i == 0:
                prime = False
                break
        if prime:
            counter += 1
    return numerator
                
            
                
