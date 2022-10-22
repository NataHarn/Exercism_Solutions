# func to check isogram
def is_isogram(string):
    string = list(string.lower())
    for char in string:
        if ord(char) in range(ord('a'), ord('z')+1):
            if string.count(char) > 1:
                return False
    return True
