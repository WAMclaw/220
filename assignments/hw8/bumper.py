"""
William McClain
bumper.py
Problem:
Affirmation: I affirm that all of this code is my own work.
"""
from random import randint
from graphics import Circle, Point, GraphWin, color_rgb, time


def get_random(int_move_amount):
    a_num = -int_move_amount
    b_num = int_move_amount
    num_ran = randint(a_num, b_num)
    return num_ran


def did_collide(circle_ball, circle_ball2):
    # Boolean output
    add_rads = circle_ball.getRadius() + circle_ball2.getRadius()
    center1 = circle_ball.getCenter()
    center2 = circle_ball2.getCenter()
    circ_dif_x = abs(center1.getX() - center2.getX())
    circ_dif_y = abs(center1.getY() - center2.getY())
    dist_centers = ((circ_dif_x ** 2) + (circ_dif_y ** 2)) ** (1 / 2)

    if add_rads >= dist_centers:
        return True
    return False


def hit_vertical(circle_ball, graphwin_win):
    # Boolean output
    rad_b = circle_ball.getRadius()
    center_b = circle_ball.getCenter()
    x_b = center_b.getX()
    width_w = graphwin_win.getWidth()
    diff_vert = width_w - x_b
    if diff_vert <= rad_b or diff_vert >= width_w - rad_b:
        return True
    return False


def hit_horizontal(circle_ball, graphwin_win):
    # Boolean output
    rad_b = circle_ball.getRadius()
    center_b = circle_ball.getCenter()
    y_b = center_b.getY()
    height_w = graphwin_win.getHeight()
    diff_horiz = height_w - y_b
    if diff_horiz in (rad_b, height_w - rad_b):  # was told to add this bit of code by the
        # test
        # original if statement (if diff_horiz == rad_b or diff_horiz == height_w - y_b:)
        return True
    return False


def get_random_color():
    val1 = randint(0, 255)
    val2 = randint(0, 255)
    val3 = randint(0, 255)
    ran_color = color_rgb(val1, val2, val3)

    return ran_color


def main():
    height = 400
    width = 600
    rad_bump1 = 30
    rad_bump2 = 30
    b1_color = get_random_color()
    b2_color = get_random_color()
    rink = GraphWin('Bumpers', width, height)
    seat1 = Point(0.25 * width, 0.5 * height)
    seat2 = Point(0.75 * width, 0.5 * height)
    bumper1 = Circle(seat1, rad_bump1)
    bumper2 = Circle(seat2, rad_bump2)
    bumper1.draw(rink)
    bumper2.draw(rink)
    bumper1.setFill(b1_color)
    bumper2.setFill(b2_color)
    x1_move = get_random(1)
    y1_move = get_random(1)
    x2_move = get_random(1)
    y2_move = get_random(1)

    while 1:
        time.sleep(0.05)
        bumper1.move(x1_move, y1_move)
        time.sleep(0.05)
        bumper2.move(x2_move, y2_move)
        if hit_horizontal(bumper1, rink):
            y1_move = -y1_move
        if hit_horizontal(bumper2, rink):
            y2_move = -y2_move
        if hit_vertical(bumper1, rink):
            x1_move = -x1_move
        if hit_vertical(bumper2, rink):
            x2_move = -x2_move
        if did_collide(bumper1, bumper2):
            x1_move = -x1_move
            y1_move = -y1_move
            x2_move = -x2_move
            y2_move = -y2_move


if __name__ == '__main__':
    main()
