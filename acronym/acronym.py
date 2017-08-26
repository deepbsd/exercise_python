def abbreviate(s):
    s = s.replace('-', ' ')
    ans=''
    for w in s.split(' '):
        ans += w[0:1].upper()
    return ans
