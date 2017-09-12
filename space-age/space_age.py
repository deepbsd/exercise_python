class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self.eo_seconds = 31557600

    def on_earth(self):
        return self.convert(1.0)

    def on_mercury(self):
        return self.convert(0.2408467)

    def on_venus(self):
        return self.convert(0.61519726)

    def on_mars(self):
        return self.convert(1.8808158)

    def on_jupiter(self):
        return self.convert(11.862615)

    def on_saturn(self):
        return self.convert(29.447498)

    def on_uranus(self):
        return self.convert(84.016846)

    def on_neptune(self):
        return self.convert(164.79132)

    def convert(self, pct_of_earth_orbit):
        return float("{0:.2f}".format(self.seconds/(self.eo_seconds*pct_of_earth_orbit)))
