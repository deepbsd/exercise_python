def verify(isbn):
    string = isbn.replace('-', '')
    if string == '' or len(string) != 10:
        return False
    num_arr = list(string)

    if num_arr[-1] == 'X':
        num_arr[-1] = '10'
    for val in num_arr:
        try:
            if int(val) not in range(0,11):
                return False
        except ValueError:
            return False

    return sum([int(num_arr[n])*(10-n) for n in range(0,9+1)]) % 11 == 0

