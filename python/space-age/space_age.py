from datetime import timedelta

class SpaceAge:
    ORBIT_PERIODS = {
            'Mercury': 0.2408467,
            'Venus': 0.6157982,
            'Earth': 1.0,
            'Mars': 1.8808158,
            'Jupiter': 11.862615,
            'Saturn': 29.447498,
            'Uranus': 84.016846,
            'Neptune': 164.79132,
        }
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(timedelta(seconds=self.seconds).days / 365.25, 2)

    def on_mercury(self):
        return round(self.on_earth() / SpaceAge.ORBIT_PERIODS['Mercury'], 2)
        
    def on_venus(self):
        return round(self.on_earth() / SpaceAge.ORBIT_PERIODS['Venus'], 2)

    def on_mars(self):
        return round(self.on_earth() / SpaceAge.ORBIT_PERIODS['Mars'], 2)

    def on_jupiter(self):
        return round(self.on_earth() / SpaceAge.ORBIT_PERIODS['Jupiter'], 2)

    def on_saturn(self):
        return round(self.on_earth() / SpaceAge.ORBIT_PERIODS['Saturn'], 2)

    def on_uranus(self):
        return round(self.on_earth() / SpaceAge.ORBIT_PERIODS['Uranus'], 2)

    def on_neptune(self):
        return round(self.on_earth() / SpaceAge.ORBIT_PERIODS['Neptune'], 2)
