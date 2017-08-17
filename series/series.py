def slices(lst, num):
    if num > len(lst) or num < 1:
        raise ValueError('Wrong size')
    results = []
    for n in range(len(lst)-(num-1)):
        try:
            results.append( [ int(i) for i in list(lst[n:n+num]) ] )
        except IndexError:
            break
    return results

