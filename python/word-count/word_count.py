def count_words(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace('\t',' ')
    sentence = sentence.replace('\n',' ')
    sentence = sentence.strip("'")
    words = list(sentence)
    for idx, letter in enumerate(words):
        if not letter.isalnum(): 
            if letter == "'":
                if not all([x.isalnum() for x in words[idx-1:idx+2:2]]):
                    words[idx] = ' '
            else:
                words[idx] = ' '
    sentence = ''.join(words)
    words = sentence.split(' ')
    words = sorted([word for word in words if word != ''])
    res = dict()
    for idx, word in enumerate(words):
        if idx == 0:
            prev_word, prev_idx = word, 0
        elif prev_word != word:
            res[prev_word] = idx - prev_idx
            prev_word, prev_idx = word, idx
        if idx == len(words) - 1:
            res[prev_word] = idx - prev_idx +1
    return res
            