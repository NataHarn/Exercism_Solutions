def rotate(text, key):
    key = key % 26 # key is 0-26
    res = []
    for t in text:
        if ord('A') <= ord(t) <= ord('Z'):
            char = chr((((ord(t) - ord('A')) + key) % 26) + ord('A'))
            res.append(char)
        elif ord('a') <= ord(t) <= ord('z'):
            char = chr((((ord(t) - ord('a')) + key) % 26) + ord('a'))
            res.append(char)
        else:
            res.append(t)  
    return ''.join(res)
