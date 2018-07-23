def verify(isbn):
    if isbn == '': 
        return False
    string = isbn.replace('-', '')
    num_arr = list(string)
    if num_arr[-1] == 'X':
        num_arr[-1] = '10'
    #print("num_arr: "+str(num_arr))
    for val in num_arr:
        if val not in range(0,10):
            return False

    return sum([int(num_arr[n]*(10-n)) for n in range(0,10)]) % 11 == 0



if __name__ == "__main__":
    nums = [
        '3-598-21508-8',
        '3-598-21508-9',
        '3-598-21507-X',
        '3-598-21507-A',
        '3-598-P1581-X',
        '3-598-2X507-9',
        '3598215088',
        '359821507X',
        '359821507',
        '3598215078X',
        '3-598-21507',
        '3-598-21507-XX',
        '3-598-21515-X',
        '',
        '134456729' ]
    for num in nums:
        print("Num: {} Val: {}".format(num, verify(num)))
    #num = "3-598-21508-8"  # True example
    #num = "3-598-21508-9"   # False example
    #print(verify(num))
