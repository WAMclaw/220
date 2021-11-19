"""
William McClain
ThreeDoorGame.py
Problem: Create a game that creates window with three door buttons for the user to open to guess the
secret door
Affirmation: I affirm that this is all my own work.
"""

from graphics import Rectangle, Point, GraphWin, Text
from button import Button

height = 500
width = 700
win = GraphWin("Three Door Game", width, height)
win.setCoords(10,10,1,1)
text_point = Point(2,5)
pointa = Point(7,7)
pointb = Point(8,8)
title = Text(text_point, "Title")
title.draw(win)

buttona = Rectangle(pointa, pointb)
buttonb = buttona.clone()
buttonb.move(-2, 0)
buttonc = buttonb.clone()
buttonc.move(-2, 0)

button1 = Button(buttona, "Door 1")
button2 = Button(buttonb, "Door 2")
button3 = Button(buttonc, "Door 3")

# center = button.getCenter()
# center.move(100,100)

button1.draw(win)
button2.draw(win)
button3.draw(win)
win.getMouse()