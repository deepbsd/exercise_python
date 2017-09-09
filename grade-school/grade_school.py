class School(object):
    def __init__(self, name):
        self.schoolname = name
        self.dict = {}

    def sort(self):
        lst = []
        for k, v in sorted(self.dict.items()):
            lst.append( (k, tuple(sorted(v))))
        return lst

    def add(self, name, ingrade):
        grade = int(ingrade)
        try:
            self.dict[grade].append(name)
        except KeyError:
            self.dict[grade] = []
            self.dict[grade].append(name)

    def grade(self, num):
        num = int(num)
        try:
            return sorted(tuple(self.dict[num]))
        except KeyError:
            return tuple([])
