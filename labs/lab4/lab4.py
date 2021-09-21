"""
Name: William McClain
lab4.py
Problem(s):
change a function, squares(), that creates circles to instead create squares and keep the squares created
create a function, rectangle(), that has a user create a rectangle and calculate the area and perimeter
create a function like rectangle(), circle(), that instead calculates the radius of the users circle
create a function, pi2(), that asks for number of terms in the sum in the pattern of 4/1 - 4/3 + 4/5 -4/7 ...
    have the function then calculate the approximation of pi

I affirm that the editing to this code is all my own work with help from the TA and LT.
"""

from graphics import *
from math import pi


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add a rectangle")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        clone_sq = shape.clone()
        clone_sq.move(dx, dy)
        clone_sq.draw(win)
    instructions.setText("Click again to quit")
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    rect_win_h = 500
    rect_win_w = 500

    win_rect = GraphWin("Rectangle", rect_win_w, rect_win_h)

    text_pt = Point(rect_win_w / 2, rect_win_h - 70)

    rect_inst = Text(text_pt, "Choose two points for your Rectangle")
    rect_inst.draw(win_rect)

    c1 = win_rect.getMouse()
    c1.draw(win_rect)
    c2 = win_rect.getMouse()
    c2.draw(win_rect)

    rect = Rectangle(c1, c2)
    rect.draw(win_rect)

    diff_x = abs(c1.getX() - c2.getX())
    diff_y = abs(c1.getY() - c2.getY())
    perimeter_rect = round(2 * (diff_x + diff_y), 2)
    area_rect = round(diff_x * diff_y, 2)

    p_rect_str = str(perimeter_rect)
    a_rect_str = str(area_rect)

    # click for close
    rect_inst.setText("Click again to quit")

    p_text_pt = Point(rect_win_w / 2, rect_win_h - 50)
    a_text_pt = Point(rect_win_w / 2, rect_win_h - 30)
    p = "Perimeter: " + p_rect_str + " pixels."
    a = "Area: " + a_rect_str + " pixels."
    rect_p_fin = Text(p_text_pt, p)
    rect_a_fin = Text(a_text_pt, a)
    rect_p_fin.draw(win_rect)
    rect_a_fin.draw(win_rect)

    win_rect.getMouse()
    win_rect.close()

    pass

def circle():
    circ_win_h = 500
    circ_win_w = 500

    win_circ = GraphWin("Circle", circ_win_w, circ_win_h)
    circ_text_pt = Point(circ_win_w / 2, circ_win_h - 70)
    circ_text_pt2 = Point(circ_win_w / 2, circ_win_h - 50)

    circ_inst = Text(circ_text_pt, "Choose two points for your circle, the first being the center point.")
    circ_inst.draw(win_circ)
    circ_inst2 = Text(circ_text_pt2, "The second point will be a point on the circumference.")
    circ_inst2.draw(win_circ)

    circ_c1 = win_circ.getMouse()
    circ_c1.draw(win_circ)
    circ_c2 = win_circ.getMouse()
    circ_c2.draw(win_circ)

    # calculate radius
    circ_dif_x = abs(circ_c1.getX() - circ_c2.getX())
    circ_dif_y = abs(circ_c1.getY() - circ_c2.getY())
    circ_radius = ((circ_dif_x ** 2) + (circ_dif_y ** 2)) ** (1/2)

    circ = Circle(circ_c1, circ_radius)
    circ.draw(win_circ)

    circ_rad_txt = str(circ_radius)

    # click for close
    circ_inst.setText("Click again to quit")
    circ_inst2.setText("")

    rad_text_pt = Point(circ_win_w / 2, circ_win_h - 30)
    rad = "Radius: " + circ_rad_txt + " pixels."
    circ_rad_fin = Text(rad_text_pt, rad)
    circ_rad_fin.draw(win_circ)

    win_circ.getMouse()
    win_circ.close()

def pi2():
    print("This will approximate pi if given a number of sums in the sequence,")
    print("[4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...]")
    print()

    app_amount = eval(input("Give [n] number of terms in the series: "))
    numer = (-4)
    denom = (-1)
    pi_approx = 0

    for i in range(app_amount):
        numer = numer * (-1)
        denom = denom + 2
        pi_approx = pi_approx + (numer/denom)

    print("Approximation of Pi: ", round(pi_approx, 5))
    varience = round(pi - pi_approx, 5)
    print("Difference from Pi: ", varience)

def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
