score_map = { 1: 'A, E, I, O, U, L, N, R, S, T',
              2: 'D, G',
              3: 'B, C, M, P',
              4: 'F, H, V, W, Y',
              5: 'K',
              8: 'J, X',
             10: 'Q, Z' }

def score(word):
    score = 0
    for letter in word:
        for key, values in score_map.items():
            if letter.upper() in values:
                score += key
                break
    return score
