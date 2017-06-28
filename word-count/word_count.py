def word_count(s):

    '''Note: values must be in the order in which they appear! '''

    values = [s.count(w) for w in set(s.split(' '))]
    outdict = dict.fromkeys(set(s.split(' ')) )

    index = 0
    for k in outdict.keys():
        outdict[k] = values[index]
        index += 1

    print(outdict)