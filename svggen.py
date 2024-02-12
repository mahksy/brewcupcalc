import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 400,400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.3,0.3,0.3)
ctx.paint()

ctx.rectangle(50,50, 200, 300)
ctx.set_source_rgb(0.1,0.1,0.1)
ctx.set_line_width(10)
ctx.stroke()

ctx.arc(250,200,100,math.pi*1.5,math.pi*2.5)

ctx.set_source_rgb(0.1,0.1,0.1)
ctx.set_line_width(10)
ctx.stroke()


surface.write_to_png('test.png')