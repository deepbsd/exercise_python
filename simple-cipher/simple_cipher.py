class Cipher(object):
    def __init__(self,key=False):
        self.alphabet = list('abcdefghijklmnopqrstuvwxyz')
        self.key = self.validatekey(key)
        self.result = []

    def encode(self, string):
        while len(self.key) < len(string):
            self.key += self.key
        for i,c in enumerate(string.lower()):
            char = self.key[i]
            offset = self.alphabet.index(char)
            if not c.isalpha():
                continue
            if self.alphabet.index(c) + offset > 25:
                self.result.append(self.alphabet[(self.alphabet.index(c)+offset)-26])
            else:
                self.result.append(self.alphabet[self.alphabet.index(c)+offset])
        return ''.join(self.result)

    def decode(self, string):
        if self.result != []:
            self.result = []
        for i,c in enumerate(string.lower()):
            char = self.key[i]
            offset = self.alphabet.index(char)
            if self.alphabet.index(c)-offset < 0:
                self.result.append(self.alphabet[self.alphabet.index(c)-offset+26])
            else:
                self.result.append(self.alphabet[self.alphabet.index(c)-offset])
        return ''.join(self.result)

    def validatekey(self,key):
        if not key:
            key = self.generatekey()
            return key
        if not (key.isalpha() and key.islower()):
            raise ValueError('All items in the key must be chars and lowercase!')
        else:
            return key

    def generatekey(self):
        from random import randint
        return ''.join([ self.alphabet[randint(0,25)] for n in range(0,100) ])



class Caesar(object):
    def __init__(self):
        self.alphabet = list('abcdefghijklmnopqrstuvwxyz')
        self.offset = 3
        self.result = []

    def encode(self, string):
        for c in list(string.lower()):
            if not c.isalpha():
                continue
            if self.alphabet.index(c)+self.offset > 25:
                self.result.append(self.alphabet[(self.alphabet.index(c)+self.offset)-26])
            else:
                self.result.append(self.alphabet[self.alphabet.index(c)+self.offset])
        return ''.join(self.result)

    def decode(self, string):
        for c in list(string.lower()):
            if self.alphabet.index(c)-self.offset < 0:
                self.result.append(self.alphabet[self.alphabet.index(c)-self.offset+26])
            else:
                self.result.append(self.alphabet[self.alphabet.index(c)-self.offset])
        return ''.join(self.result)
