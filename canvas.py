from tkinter import *
root = Tk()
canvas_width = 500
canvas_height = 500
c = Canvas(root, width=canvas_width, height=canvas_height)
c.pack()
y = int(canvas_height/2)
c.create_line(10, y, canvas_width, y, fill="Green")
coord = 10, 50, 240, 210
arc = c.create_arc(coord, start=90, extent=190, fill="red")
oval = c.create_oval(50, 60, 100, 100)
