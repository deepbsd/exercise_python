import re

alpha=list('abcdefghijklmnopqrstuvwxyz')
reverse=list(reversed(alpha))

def encode(s):
    length=5
    ans = ''
    for c in re.sub(r'[ \W]', '', s):
        if c.isupper():
            ans += reverse[alpha.index(c.lower())]
        elif c.isdigit():
            ans += c
        else:
            ans += reverse[alpha.index(c)]

    ans = ' '.join([ans[i:i+length] for i in range(0, len(ans), length) ] )
    return ans


def decode(s):
    ans = ''
    for c in re.sub(r' ', '', s):
        if c.isdigit():
            ans += c
        else:
            ans += alpha[reverse.index(c)]
    return ans
