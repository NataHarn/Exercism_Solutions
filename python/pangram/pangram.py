# check for pangram
def is_pangram(sentence):
    sentence = sentence.lower()
    sentence_lst = list(sentence)
    for asc in range(ord('a'), ord('z')+1):
        if sentence_lst.count(chr(asc)) == 0:
            return False
    return True
