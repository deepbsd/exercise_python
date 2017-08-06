from re import sub

def decode(text):

    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)),
               text)


def encode(text):

    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1) if len(m.group(0)) > 1 else str(m.group(1)),
               text)
