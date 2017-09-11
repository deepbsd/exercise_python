def numeral(num):

    romans = list(reversed(['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']))
    integers = list(reversed([1,4,5,9,10,40,50,90,100,400,500,900,1000]))

    result = ''

    for n in range(len(integers)):
        count = int(num/integers[n])
        result += romans[n] * count
        num -= integers[n] * count

    return result

if __name__ == "__main__":
    for n in range(1,3001):
        print(n,': ',numeral(n))
