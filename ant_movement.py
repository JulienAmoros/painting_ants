from random import *

"""
0=N
1=NE
2=E
3=SE
4=S
5=SW
6=W
7=NW
"""


class AntMovement:
    def __init__(self, probs, type='O'):
        if type == 'D':
            self.direction = randint(0, 3)*2
            self.turn_angle = 2
        else:
            self.direction = randint(0, 7)
            self.turn_angle = 1

        self.probs = probs
        prob_total = 0
        for k, v in self.probs.items():
            prob_total += v
        for k, v in self.probs.items():
            self.probs[k] = v/prob_total

    def move(self):
        var_alea = random()
        for k, v in self.probs.items():
            var_alea -= v
            if var_alea < 0:
                if k == 'G':
                    self.direction -= self.turn_angle
                if k == 'D':
                    self.direction += self.turn_angle
                break
        if self.direction <= -1:
            self.direction += 8
        if self.direction >= 8:
            self.direction -= 8
