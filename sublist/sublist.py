def check_lists(first_list, second_list):
    if len(first_list) > len(second_list):
    	A, B = first_list, second_list
    else:
    	A, B = second_list, first_list

	for n in range(len(B)):
		if A[n:len(A)] == B[n:len(A)]:
			return SUPERLIST
	for n in range(len(A)):
		if B[n:len(B)] == A[n:len(B)]:
			return SUBLIST
			

