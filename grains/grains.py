def on_square(num):
    if num <= 64 and num > 0:
        return 2**(num-1)
    else:
        raise ValueError


def total_after(num):
    if num <= 64 and num > 0:
        return sum([2**(n-1) for n in range(1,num+1)])
    else:
        raise ValueError
