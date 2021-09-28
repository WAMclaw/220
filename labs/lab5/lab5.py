"""
Name: William McClain
lab5.py

I affirm that the code below is my own work with help from the TA and the LT.
"""

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)
    text_point = Point(250, 400)
    txt_p2 = Point(250, 450)
    txt_p3 = Point(250, 475)
    instruct1 = Text(text_point, "Click Three Times")
    instruct1.draw(win)

    # Add code here to accept the mouse clicks, draw the triangle.
    tri_p1 = win.getMouse()
    tri_p1.draw(win)
    tri_p2 = win.getMouse()
    tri_p2.draw(win)
    tri_p3 = win.getMouse()
    tri_p3.draw(win)

    user_tri = Polygon(tri_p1, tri_p2, tri_p3)
    user_tri.draw(win)

    dx1 = abs(tri_p1.getX() - tri_p2.getX()) ** 2
    dx2 = abs(tri_p2.getX() - tri_p3.getX()) ** 2
    dx3 = abs(tri_p3.getX() - tri_p1.getX()) ** 2
    dy1 = abs(tri_p1.getY() - tri_p2.getY()) ** 2
    dy2 = abs(tri_p2.getY() - tri_p3.getY()) ** 2
    dy3 = abs(tri_p3.getY() - tri_p1.getY()) ** 2

    length_a = (dx1 + dy1) ** (1/2)
    length_b = (dx2 + dy2) ** (1/2)
    length_c = (dx3 + dy3) ** (1/2)

    tri_s = (length_a + length_b + length_c) / 2
    tri_perimeter = round(tri_s * 2, 3)
    tri_area = round((tri_s * (tri_s - length_a) * (tri_s - length_b) * (tri_s - length_c)) ** (1/2), 3)
    # and display its area in the graphics window.
    perimeter_txt = Text(txt_p2, "The Perimeter: " + str(tri_perimeter))
    perimeter_txt.draw(win)
    area_txt = Text(txt_p3, "The Area: " + str(tri_area))
    area_txt.draw(win)
    # Wait for another click to exit
    instruct1.setText("Click again to close.")
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_value_pt = red_text_pt.clone()
    red_value_pt.move(50, 0)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_value = Entry(red_value_pt, 5)
    red_value.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_value_pt = green_text_pt.clone()
    green_value_pt.move(50, 0)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_value = Entry(green_value_pt, 5)
    green_value.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_value_pt = blue_text_pt.clone()
    blue_value_pt.move(50, 0)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_value = Entry(blue_value_pt, 5)
    blue_value.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for _ in range(5):
        win.getMouse()
        r = int(red_value.getText())
        g = int(green_value.getText())
        b = int(blue_value.getText())
        circle_color = color_rgb(r, g, b)
        shape.setFill(circle_color)


    # Wait for another click to exit
    inst.setText("Click again to close the window")
    win.getMouse()
    win.close()

def process_string():
    string = str(input("Give a string: "))
    first = string[0]
    last = string[-1]
    throu_25 = string[1:5]
    con = str(first) + str(last)
    rep3 = string[0:2] * 10
    length = len(string)

    print(first)
    print(last)
    print(throu_25)
    print(con)
    print(rep3)
    for i in range(length-1):
        print(string[i])
    print(length)

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x[2] = values[0]
    print(x)
    x[1:] = [values[0], eval(values[5])]
    print(x)
    x = sum(x)
    print(x)
    x = len(values)
    print(x)


def another_series():
    n = eval(input("Enter the number of terms to be added: "))
    vals = [6, 4, 2]
    ph = 0
    x = 3
    for i in range(n):
        x = x + 2
        ph = x%3

        print(ph)

def main():
    # target()
    # triangle()
    # color_shape()
    # process_string()
    # process_list()
    # another_series()
    pass


main()
