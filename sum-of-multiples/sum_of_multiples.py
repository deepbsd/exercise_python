def sum_of_multiples(num, arr):
	multiples = []
	for i in range(1,num):
		for n in arr:
			if i%n==0:
				multiples.append(i)
	multiples = set(multiples)
	return sum(multiples)

    
