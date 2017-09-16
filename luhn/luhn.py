import re

class Luhn(object):
    '''Peforms number validation for credit cards, etc.'''
    def __init__(self, string):
        self.number = string
        self.total = self.get_sum(string)

    def get_sum(self, string):
        '''returns the sum of adjusted digits in number string'''
        num = int(re.sub('[^0-9]', '', string))
        numlist = [ int(n) for n in reversed(str(num)) ]
        for n in range(1,len(numlist),2):
            if (numlist[n]*2) > 9:
                numlist[n] = (numlist[n] * 2) - 9
            else:
                numlist[n] = numlist[n] * 2
        return sum(numlist)

    def is_valid(self):
        '''returns true if valid number and evenly divisible by 10'''
        if len(self.number) <= 1:
            return False
        if not self.number.replace(" ","").isdigit():
            return False
        else:
            return self.total % 10 == 0
