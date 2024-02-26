import turtle as t

def draw(t, shape):
    t.color('white')  
    t.bgcolor('black') 
    if shape == 'square':
        degree = 90
    elif shape == 'pentagon':
        degree = 72
    elif shape == 'octagon':
        degree = 45
    for i in range(200):        
        t.right(degree)
        t.fd(1 + i)

t.hideturtle()
shape = input('What shape do you want to draw?: ')
draw(t, shape)
t.mainloop()