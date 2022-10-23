def find_anagrams(word, candidates):
    word = word.lower()
    anagram = []
    word_lst = sorted(list(word))
    for candidate in candidates:
        candidate_lst = sorted(list(candidate.lower()))
        if candidate_lst == word_lst and candidate.lower() != word:
            anagram.append(candidate)
    return anagram
