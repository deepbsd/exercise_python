
"""Transcribe a DNA strand to an RNA strand.  Return
empty string if input is invalid.
"""
def to_rna(strand):
    string = ''
    for c in strand:
        if c == 'G': string += 'C'
        if c == 'C': string += 'G'
        if c == 'T': string += 'A'
        if c == 'A': string += 'U'

    return string if len(string) == len(strand) else ''


