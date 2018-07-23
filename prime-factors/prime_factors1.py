

def prime_factors(num):
    from math import sqrt

    def gen_primes(n):
        if n == 0 or n == 1:
            return []
        else:
            p = gen_primes(int(sqrt(n)))
            no_p = {j for i in range(2,int(sqrt(n))) for j in range(i*2, n+1, i)}
            p = {x for x in range(2, n+1) if x not in no_p}
        return p

    result = []
    primes = gen_primes(num)

    for factor in primes:
        while num%factor == 0:
            num /= factor
            result.append(factor)
            if num == 1:
                break
    return result
