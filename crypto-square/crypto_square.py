import re
import math

def encode(plaintext):
    newtext = plaintext.lower()
    newtext = re.sub(r'[^a-z0-9]', '', newtext)
    length = len(newtext)
    size = int(math.ceil(math.sqrt(length)))
    coded = [newtext[n::size] for n in range(size)]

    return ' '.join([''.join(c) for c in coded])


