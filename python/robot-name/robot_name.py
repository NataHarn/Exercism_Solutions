from random import randint, seed
import time

class Robot:
    RobotsNames = []
    def __init__(self):
        seed(time.time() *1000 %1000)
        self.name = self._generate_name()
        Robot.RobotsNames.append(self.name)
        print(self.name)
        
    def _get_name(self):
        return self._rand_char() + self._rand_char() + str(randint(000, 999)).zfill(3)
        
    def _generate_name(self):
        name = self._get_name()
        while name in Robot.RobotsNames:
            name = self._get_name()
        return name
        
    def reset(self):
        Robot.RobotsNames.remove(self.name)
        self.name = self._generate_name()

    def _rand_char(self):
        return chr(randint(ord('A'), ord('Z')))
        