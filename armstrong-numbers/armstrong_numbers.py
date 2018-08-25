def is_armstrong(number):
    power = len(str(number))
    return sum([int(n)**power for n in str(number)]) == number
