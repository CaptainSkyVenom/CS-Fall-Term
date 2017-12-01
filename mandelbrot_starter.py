# Original code from:
# http://code.activestate.com/recipes/578590-mandelbrot-fractal-using-tkinter/

# import the libraries you'll need
import tkinter
from tkinter import *

def escaped(z1, z2, c1, c2, it):
    if it >= 254:
        return it
    if z1**2 + z2**2 >= 4:
        return it
    else:
        return escaped((z1**2 - z2**2) + c1, 2 * z1 * z2 + c2, c1, c2, it+1);


# variables we will use throughout the program
WIDTH = 640 # width and height of our picture in pixels
HEIGHT = 640
maxIt = 255 # max iterations; corresponds to color

# create a new Tkinter window
window = Tk()
window2 = Toplevel()
window3 = Toplevel()


# create a canvas, and place it in the window
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "#000000")
canvas2 = Canvas(window2, width = WIDTH, height = HEIGHT, bg = "#000000")
canvas3 = Canvas(window3, width = WIDTH, height = HEIGHT, bg = "#000000")

# set up the canvas so it can hold a picture
img = PhotoImage(width = WIDTH, height = HEIGHT)
img2 = PhotoImage(width = WIDTH, height = HEIGHT)
img3 = PhotoImage(width = WIDTH, height = HEIGHT)

canvas.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)
canvas2.create_image((0, 0), image = img2, state = "normal", anchor = tkinter.NW)
canvas3.create_image((0, 0), image = img3, state = "normal", anchor = tkinter.NW)


# loop through all the pixels in the image

prime = []
for i in range(500000):
    prime.append(1)

for p in range(2, 650):
    if prime[p] == 1:
        for i in range(p*2, 500000, p):
            prime[i] = 0

prime[0] = 0
prime[1] = 0

for row in range(HEIGHT):
    for col in range(WIDTH):

        xmin = -2 # the zoom we want to see
        xmax = 2
        ymin = -2
        ymax = 2
        #r = escaped(0,0, xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * (HEIGHT-row) / HEIGHT,0)
        r = escaped(xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * row / HEIGHT, -0.742, 0.1,0)

        rd = hex(r*400*prime[row*640+col]%256)[2:].zfill(2)
        gr = hex(r*400*prime[row*640+col]%256)[2:].zfill(2)
        bl = hex(r*400*prime[row*640+col]%256)[2:].zfill(2)


        img.put("#" + rd + gr + bl, (col, row))

for row in range(HEIGHT):
    for col in range(WIDTH):

        xmin = -0.723173919260 # the zoom we want to see
        xmax = -0.722910572111
        ymin = 0.237466613173
        ymax = 0.237729960322

        r = escaped(0,0, xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * row / HEIGHT,0)
        #r = escaped(xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * (HEIGHT-row) / HEIGHT, 0.687, 0.312,0)

        rd = hex((r*40 + (row*WIDTH + col)//100)%256)[2:].zfill(2)
        gr = hex((r*24 + (row*WIDTH + col)//100)%256)[2:].zfill(2)
        bl = hex((r*30 + (row*WIDTH + col)//100)%256)[2:].zfill(2)

        if r >= 254:
            rd = '00'
            gr = rd
            bl = gr

        img2.put("#" + rd + gr + bl, (col, row))

fib = [0,1]
for i in range(256):
    fib.append(fib[i] + fib[i+1])

for row in range(HEIGHT):
    for col in range(WIDTH):
        xmin = -0.430139 # the zoom we want to see
        xmax = -0.414636
        ymin = 0.570945
        ymax = 0.58644818
        r = escaped(0,0, xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * (HEIGHT-row) / HEIGHT,0)
        #julia r = escaped(xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * row / HEIGHT, 0.687, 0.312,0)

        rd = hex(256-(r*fib[r]**prime[r])%256)[2:].zfill(2)
        gr = hex(256-(r*fib[r]**prime[r])%256)[2:].zfill(2)
        bl = hex(256-(r*fib[r]**prime[r])%255)[2:].zfill(2)



        img3.put("#" + rd + gr + bl, (col, row))


# update the canvas and display our drawing
canvas.pack()
canvas2.pack()
canvas3.pack()
mainloop()
