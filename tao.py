import turtle as t
from random import random

t.Pen()
t.shape('turtle')
colors =['pink', 'lightgreen', 'white', 'skyblue', 'red', 'orange', 'khaki']
t.bgcolor('black')

for i in range(300):
    t.color(colors[int(random() * len(colors))])
    t.right(90)
    t.fd(1 + i)

t.hideturtle()
t.mainloop()