from turtle import *

speed(-1)
for i in range(3, 10):
    if i % 2 == 0:
        color('blue')
    else:
        color('red')
    for j in range(i):
        forward(100)
        left(360/i)
mainloop()
