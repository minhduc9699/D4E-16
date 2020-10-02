from turtle import *

shape('turtle')
color('green')
speed(-1)

# for i in range(3):
#     forward(100) # drawing
#     left(90)
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)
#     forward(100)

#     left(30)

for i in range(800):
    for i in range(4):
        forward(100)
        left(90)
    right(7)
mainloop() # keep window open
