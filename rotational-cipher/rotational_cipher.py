def rotate(str, n):
    output = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in str:
        if c not in alpha and c not in alpha1:
            output += c
            continue
        if c.isupper():
            coll = alpha1
        else:
            coll = alpha
        try:
            output += coll[coll.index(c)+n]
        except IndexError:
            output += coll[coll.index(c)-(26-n)]

    return output
