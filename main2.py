from turtle import *
import colorsys

bgcolor('black')
pensize(2)
speed(-5)
h = 0.7  # Start with a different hue

for i in range(300):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.005  # Slower hue increment for a smoother gradient

    # Different design pattern
    fd(i * 0.75)
    lt(45)
    fd(i * 0.25)
    rt(135)
    
    for j in range(3):
        fd(i * 0.2)
        lt(120)
    rt(60)  # Additional rotation for the next iteration

done()
