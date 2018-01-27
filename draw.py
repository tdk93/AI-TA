
import numpy as np
from time import time
from tkinter   import Tk, Canvas
from random import randint

screenSize = 700
################################ DRAWING METHODS #################################

def randColor():
	return "#%06x" % randint(0,0xFFFFFF)

def drawPath(cities, path, length):
	#cities = cities[ path ]
	#print("cities:", cities)
	#print("path:", path) 
	msg = "Length*: {:.2E}".format(length)
	canvas.create_text(screenSize/2, screenSize+50, text = msg, fill = 'black',  font = ('Helvetica', 20, 'bold'))
	
	addToCanvas(cities, path)
	canvas.update()
	root.mainloop()

def addToCanvas(cities, path):
	min_x = cities[path[0]].x
	min_y = cities[path[0]].y
	max_x = cities[path[0]].x
	max_y = cities[path[0]].y	
	for i in range(1, len(path)):
		if cities[path[i]].x < min_x:
			min_x = cities[path[i]].x
		if cities[path[i]].y < min_y:
			min_y = cities[path[i]].y

		if cities[path[i]].x > max_x:
			max_x = cities[path[i]].x
		if cities[path[i]].y > min_y:
			max_y = cities[path[i]].y


	for i in range( len( path ) ):
		c = cities[path[i-1]]
		c_next = cities[path[i]]

		scaled_x = (c.x - min_x) / (max_x - min_x) *2000 #screenSize + 20
		scaled_y = (c.y - min_y) / (max_y - min_y) *1000 #screenSize + 20
		scaled_x_next = (c_next.x - min_x) / (max_x - min_x) *2000# screenSize + 20
		scaled_y_next = (c_next.y - min_y) / (max_y - min_y) *1000# screenSize + 20
		print(scaled_x, scaled_y, scaled_x_next, scaled_y_next)
		canvas.create_oval( scaled_x - 4 , scaled_y - 4 , scaled_x + 4  , scaled_y + 4 , fill = randColor() , outline = 'black' )
		canvas.create_oval( scaled_x_next - 4 , scaled_y_next - 4 , scaled_x_next + 4  , scaled_y_next + 4 , fill = randColor() , outline = 'black' )

		canvas.create_text(scaled_x+8, scaled_y+8, font=("Helvetica", 10), text=str(path[i]))
		canvas.create_line( scaled_x, scaled_y , scaled_x_next, scaled_y_next , fill = 'black' )


root = Tk()
canvas = Canvas( root , width = screenSize + 40, height = screenSize + 100 , bg = 'white' )
canvas.pack()

if __name__ == "__main__":
	main()
