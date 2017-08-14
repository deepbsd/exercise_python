def detect_anagrams(word, array):
    return [ wd for wd in array if word.lower() != wd.lower() and sorted(word.lower()) == sorted(wd.lower()) ] 
