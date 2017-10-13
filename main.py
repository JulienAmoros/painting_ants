from tkinter import *
from ant_loader import load_json
from ant import *

fenetre = Tk()

json = load_json("params.json")

WIDTH = json['canvas_width']
HEIGHT = json['canvas_height']

canvas = Canvas(fenetre, width=WIDTH, height=HEIGHT)
canvas.pack()

res = ant_builder(canvas, json['ants'], json['steps'], WIDTH, HEIGHT)

for ant in res:
    ant.start()


print(canvas.find_closest(125, 125))

mainloop()
