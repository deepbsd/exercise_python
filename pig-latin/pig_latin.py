def translate(word):
    if ' ' in word:
        word = word.split(' ')
        string = ''
        for w in word:
            string += translate(w) + ' '
        return string.rstrip()
    if word[0] in 'aeiou':
        return word + 'ay'
    elif word[0:3] in ['squ', 'thr', 'sch']:
        return word[3:] + word[0:3] + 'ay'
    elif word[0:2] in ['qu', 'ch', 'sh', 'sk', 'th']:
        return word[2:] + word[0:2] + 'ay'
    elif word[0:2] in ['yt', 'xr']:
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'
