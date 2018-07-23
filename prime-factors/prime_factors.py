def prime_factors(num):
    result = []
    factor = 2
    while num > 1:
        if num%factor == 0:
            result.append(factor)
            num /= factor
        else:
            factor += 1
    return result
