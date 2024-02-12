import cairo
import math

ratio = 10

percentcoffee= 1/ratio*100
percentwater= 100-percentcoffee
hwater=(280/100)*percentwater
hcoffee =(280/100)*percentcoffee

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 400,400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.3,0.3,0.3)
ctx.paint()

ctx.rectangle(50,50, 200, 300)
ctx.set_source_rgb(0.1,0.1,0.1)
ctx.set_line_width(20)
ctx.stroke()

ctx.arc(250,200,100,math.pi*1.5,math.pi*2.5)

ctx.set_source_rgb(0.1,0.1,0.1)
ctx.set_line_width(20)
ctx.stroke()

ctx.rectangle(60,60,180,hwater)
ctx.set_source_rgb(0.11,0.64,0.93)
ctx.fill()

ctx.rectangle(60,hwater+60,180,hcoffee)
ctx.set_source_rgb(0.39,0.25,0.20)
ctx.fill()

surface.write_to_png('cup.png')

print(percentwater)