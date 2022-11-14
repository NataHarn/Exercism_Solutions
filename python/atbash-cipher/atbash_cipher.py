def encode(plain_text):
    plain_text = plain_text.lower()
    ciphers = []
    for letter in plain_text:
        encoded = translate(letter)
        if encoded != None:
            ciphers.append(translate(letter))
    ciphers = [''.join(ciphers[k:k+5]) for k in range(0, len(ciphers), 5)]
    return ' '.join(ciphers)


def decode(ciphered_text):
    return ''.join([translate(letter) for letter in ciphered_text if letter != ' '])

# both encode and decode text
def translate(letter):
    if ord('a') <= ord(letter) <= ord('z'):
        if ord(letter) < (ord('a') + ord('z')) / 2:
            return chr(ord('z') - (ord(letter)-ord('a')))
        else:
            return chr(ord('a') + (ord('z')-ord(letter)))
    elif ord('0') <= ord(letter) <= ord('9'):
        return letter
    return None