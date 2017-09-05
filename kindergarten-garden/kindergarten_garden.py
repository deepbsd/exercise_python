students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", 
   "Harriet","Ileana", "Joseph", "Kincaid",  "Larry"]

plants = {"G":"Grass", "C":"Clover", "R":"Radishes", "V":"Violets"}

class Garden(object):
    def __init__(self, object, students=students):
        self.row1 = object[0:object.index('\n')]
        self.row2 = object[object.index('\n')+1:]
        self.students = sorted(students)

    def plants(self, name):
        return [ plants[p] for p in self.row1[self.students.index(name)*2:self.students.index(name)*2+2]
               +self.row2[self.students.index(name)*2:self.students.index(name)*2+2] ]


if __name__ == "__main__":
  garden = Garden("VCRRGVRG\nRVGCCGCV",students="Samantha Patricia Xander Roger".split())
  print(garden.plants("Patricia"))
