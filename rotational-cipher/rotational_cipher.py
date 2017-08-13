def rotate(str, k):
    # figured out how to use the maketrans/translate function...
    from_string = 'abcdefghijklmnopqrstuvwxyz'
    # create a target translation table
    to_string = from_string[k:] + from_string[:k]
    # add the upper case letters to both source and target
    from_string += from_string.upper()
    to_string += to_string.upper()
    # here's the table for the translate function
    table = str.maketrans(from_string, to_string)
    # and finally, return the translation with the table as the argument
    return str.translate(table)
