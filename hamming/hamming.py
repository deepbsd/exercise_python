"""
"Hamming distance" is the number of differences between two homologous
DNA strans taken from different genomes with a different ancestor.
The strands must be of equal length.
"""
def distance(s1, s2):
    if len(s1) != len(s2): raise ValueError('Strings not equal length.')
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: count += 1
    return count
