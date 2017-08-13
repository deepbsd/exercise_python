def detect_anagrams(word, array):
    anagrams = []
    for wd in array:
        if len(word) != len(wd):
            continue
        if word.lower() == wd.lower():
            continue
        else:
            if sorted(list(word.lower())) == sorted(list(wd.lower())):
                anagrams.append(wd)
            else:
                continue
    return anagrams
