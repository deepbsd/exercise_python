def is_pangram(S):
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if S.lower().count(c) < 1: return False;

    return True;
