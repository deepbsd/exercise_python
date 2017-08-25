NORTH="NORTH"
SOUTH="SOUTH"
EAST="EAST"
WEST="WEST"

direction = [NORTH, EAST, SOUTH, WEST]

class Robot(object):

    def __init__(self, bearing=NORTH, EW=0, NS=0):
        self.bearing = bearing
        self.EW = EW
        self.NS = NS
        self.coordinates = (self.EW, self.NS)

    def turn_right(self):
        dir_index = direction.index(self.bearing)
        if (dir_index == 3): 
            dir_index = 0
            self.bearing = direction[dir_index]
        else: 
            self.bearing = direction[dir_index+1]

    def turn_left(self):
        dir_index = direction.index(self.bearing)
        if (dir_index == 0):
            dir_index = 3
            self.bearing = direction[dir_index]
        else:
            self.bearing = direction[dir_index-1]

    def advance(self):
        if self.bearing == NORTH:
            self.NS += 1
        elif self.bearing == EAST:
            self.EW += 1
        elif self.bearing == SOUTH:
            self.NS -= 1
        elif self.bearing == WEST:
            self.EW -= 1
        self.coordinates = (self.EW, self.NS)

    def simulate(self, commands):
        for c in commands:
            if c == 'L':
                self.turn_left()
                continue
            elif c == 'R':
                self.turn_right()
                continue
            elif c == 'A':
                self.advance()
                continue
            else:
                break