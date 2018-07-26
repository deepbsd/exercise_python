SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'

def check_lists(first_list, second_list):

    A, B = first_list, second_list

    if A == B:
        return EQUAL

    for n in range(len(B)):
        if A == B[n:n+len(A)]:
            return SUBLIST
    for n in range(len(A)):
        if B == A[n:n+len(B)]:
            return SUPERLIST
    return UNEQUAL


