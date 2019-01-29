from random import choice, randint
from string import ascii_uppercase
import random

class Robot(object):
    def __init__(self):
        self.name = self._create_name()

    def _create_name(self):
        return ''.join(choice(ascii_uppercase) for i in range(2))+str(randint(100,999))

    def reset(self):
        self.name = self._create_name()


if __name__ == "__main__":
    random.seed('totally random')
    robby = Robot()
    print(robby.name)
    random.seed('totally random')
    robby.reset()
    print(robby.name)
