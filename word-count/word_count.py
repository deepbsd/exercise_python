"""Counts words and returns a dict with a count of their respective occurences"""
def word_count(s):
    import re
    s = s.lower()  # lowercase all
    s = re.sub('(\w),(\w)', "\\1 \\2",s)   # inserts a space between two words joined by a comma
    s = re.sub(r'[^\w\s]', '',s)     # remove everything that isn't a word or space
    s = re.sub(r'[\n\t_]|[\s]{2,20}', ' ',s)  # replaces tabs, newlines, and multiple spaces

    outdict = { i:list(s.split(' ')).count(i) for i in list(set(s.split(' '))) }


    return outdict
