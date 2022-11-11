def abbreviate(words):
    words = words.replace('-', ' ')
    words = words.replace('_', ' ')
    words = words.title().split(' ')
    return ''.join([word[0] for word in words if word != ''])
