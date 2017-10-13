import threading
from ant_movement import *

STEPS = 0
WIDTH = 0
HEIGHT = 0


class Ant(threading.Thread):
    def __init__(self, canvas, color_painted, color_followed, movement, follow_probability):
        threading.Thread.__init__(self)
        self.canvas = canvas
        self.color_painted = "#%02x%02x%02x" % (int(color_painted[0]), int(color_painted[1]), int(color_painted[2]))
        self.color_followed = color_followed
        self.movement = movement
        self.follow_probability = follow_probability
        self.x = int(WIDTH/2)
        self.y = int(HEIGHT/2)

    def run(self):
        for i in range(0, STEPS):
            self.movement.move()
            self.apply_move(self.movement.direction)
            self.canvas.create_oval(self.x, self.y, self.x, self.y, fill=self.color_painted, outline="")

    def apply_move(self, dir):
        if dir == 0:
            self.x += 0
            self.y += 1
        if dir == 1:
            self.x += 1
            self.y += 1
        if dir == 2:
            self.x += 1
            self.y += 0
        if dir == 3:
            self.x += 1
            self.y += -1
        if dir == 4:
            self.x += 0
            self.y += -1
        if dir == 5:
            self.x += -1
            self.y += -1
        if dir == 6:
            self.x += -1
            self.y += 0
        if dir == 7:
            self.x += -1
            self.y += 1

        if self.x < 0:
            self.x += WIDTH-1
        if self.x > WIDTH:
            self.x = 0

        if self.y < 0:
            self.y += HEIGHT-1
        if self.y > HEIGHT:
            self.y = 0


def ant_builder(canvas, ant_list, steps, width, height):
    global STEPS
    global WIDTH
    global HEIGHT
    STEPS = steps
    WIDTH = width
    HEIGHT = height
    res = []
    for ant in ant_list:
        tmp = ant['color_painted']
        color_painted = (tmp['R'], tmp['G'], tmp['B'])
        tmp = ant['color_followed']
        color_followed = (tmp['R'], tmp['G'], tmp['B'])
        tmp = ant['movement']
        mov = AntMovement(tmp['probability'], tmp['type'])
        follow_probability = ant['follow_probability']
        res.append(Ant(canvas, color_painted, color_followed, mov, follow_probability))
    return res
