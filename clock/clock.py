class Clock(object):
    def __init__(self, hour, minute):
        hour += minute // 60
        self.hour = hour % 24
        self.minute = minute % 60

    def __repr__(self):
        return "{:02}:{:02}".format(self.hour, self.minute)

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        return Clock(self.hour, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minutes - minutes)
