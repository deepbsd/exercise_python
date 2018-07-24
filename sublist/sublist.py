SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'

def check_lists(first_list, second_list):

    A, B = first_list, second_list

    if A == B:
        return 'EQUAL'

    for n in range(len(B)):
        if A[n:len(A)] == B[n:len(A)]:
            return 'SUBLIST'
    for n in range(len(A)):
        if B[n:len(B)] == A[n:len(B)]:
            return 'SUPERLIST'
    if len(A) == len(B):
        for n in range(len(A)):
            if A[n] != B[n]:
                return 'UNEQUAL'


if __name__ == "__main__":
    first = [1, 2, 5]
    second = [0, 1, 2, 3, 1, 2, 5, 6]
    print(check_lists(first, second))
