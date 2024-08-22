from turtle import*
import colorsys
bgcolor('black')
pensize(2)
speed(0)
h=0.5

for i in range(200):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    rt(10)

    for j in range(5):
        fd(i)
        rt(20*5) 
rt(120)  
done()    
