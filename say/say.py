def say(num):
    up2_20 = { 0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
            10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 
            18:'eighteen', 19:'nineteen' }
    tens = [ 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']



    def hundreds(n1, n2): return n1+'-hundred '+n2
    def thousands(n1, n2): return n1+'-thousand '+n2
    def millions(n1, n2): return n1+'-million '+n2
    def billions(n1, n2): return n1+'-billion '+n2
    def trillions(n1, n2): return n1+'-trillion '+n2


    if num < 20:
        return up2_20[num]
    if (num >= 20) and (num <= 100):
        s1 = str(num)[0]
        s2 = str(num)[1:]
        return hundreds(s1, s2)

    




if __name__ == "__main__":

    print(say(233))