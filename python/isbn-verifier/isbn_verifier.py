def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    isbn_sum = 0
    for idx, digit in enumerate(isbn[:-1]):
        try:
            isbn_sum += int(digit) * (10 - idx)
        except:
            return False
    if isbn[-1] == 'X':
        isbn_sum += 10
    else:
        try:
            isbn_sum += int(isbn[-1])
        except:
            return False
    if isbn_sum % 11 == 0:
        return True
    else:
        return False
        
