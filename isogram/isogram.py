"""
If the string passed in is an isogram, the function returns true.
Basic check is done to lower case letters, remove spaces and hyphens.
"""
def is_isogram(text):
    text = text.lower().replace('-', '')
    return len(list(text.replace(' ', ''))) == len(set(list(text.replace(' ', ''))))