"""
William McClain
greeting.py

Problem:
Affirmation: I affirm that the following code is all my own work.
"""
from graphics import GraphWin, Point, Circle, Polygon, Text, color_rgb, time

# colors
pink = color_rgb(255, 192, 203)
deep_pink = color_rgb(255, 20, 147)
grey_blue = color_rgb(119, 136, 153)
light_cyan = color_rgb(224, 255, 255)
alice_blue = color_rgb(240, 248, 255)
crimson_red = color_rgb(220, 20, 60)
dark_red = color_rgb(139, 0, 0)
goldenrod = color_rgb(218, 165, 32)
midnight_blue = color_rgb(25, 25, 112)

# basic set up
C_HEIGHT = 500
C_WIDTH = 400
card = GraphWin('Greetings', C_WIDTH, C_HEIGHT)
card.setBackground(pink)

# points and shapes
pcirc1 = Point(150, 200)
point1 = Point(120, 240)
point2 = Point(200, 200)
point4 = Point(200, 350)
point3 = Point(280, 240)
pcirc3 = Point(200, 250)
circ1 = Circle(pcirc1, 50)
circ2 = circ1.clone()
circ2.move(100, 0)
big_poly = Polygon(point1, point2, point3, point4)
# poly1 = Polygon(point1, point2, point4)
poly2 = Polygon(point2, point3, point4)
circ3 = Circle(pcirc3, 52)
# arrow
ap1 = Point(120, 310)
ap2 = Point(95, 310)
ap3 = Point(105, 320)
ap4 = Point(65, 360)
ap5 = Point(58, 360)
ap6 = Point(44, 370)
ap7 = Point(55, 375)
ap8 = Point(56, 387)
ap9 = Point(71, 374)
ap10 = Point(70, 365)
ap11 = Point(110, 325)
ap12 = Point(120, 335)
arrow = Polygon(ap1, ap2, ap3, ap4, ap5, ap6, ap7, ap8,ap9, ap10, ap11, ap12)
star_p1 = Point(200, 199)
star_p2 = Point(162, 285)
star_p3 = Point(250, 230)
star_p4 = Point(150, 230)
star_p5 = Point(236, 285)
star = Polygon(star_p1, star_p2, star_p3, star_p4, star_p5)

# text
top_txt_p = Point(C_WIDTH / 2, 50)
bottom_txt_p = Point(C_WIDTH / 2, 450)
top_txt = Text(top_txt_p, "Happy Valentines Day!")
bottom_txt = Text(bottom_txt_p, "Would you be mine?")
top_txt.setTextColor(crimson_red)
bottom_txt.setTextColor(crimson_red)
top_txt.draw(card)
bottom_txt.draw(card)

# coloring shapes
# poly1.setFill(light_cyan)
# poly1.setOutline(alice_blue)
big_poly.setFill(deep_pink)
poly2.setFill(deep_pink)
circ1.setFill(deep_pink)
circ2.setFill(deep_pink)
big_poly.setOutline(deep_pink)
poly2.setOutline(deep_pink)
circ1.setOutline(deep_pink)
circ2.setOutline(deep_pink)
arrow.setFill(crimson_red)
arrow.setOutline(dark_red)
circ3.setOutline(dark_red)
star.setOutline(alice_blue)

# drawing
circ1.draw(card)
# circ2.draw(card)
# point1.draw(win)
# point2.draw(win)
# point3.draw(win)
# point4.draw(win)
# poly1.draw(win)
big_poly.draw(card)
arrow.draw(card)
circ2.draw(card)
poly2.draw(card)

# moving arrow
time.sleep(1)
for i in range(400):
    time.sleep(0.001)
    arrow.move(1, -1)

circ3.draw(card)
time.sleep(0.5)
big_poly.setOutline(dark_red)
poly2.setOutline(dark_red)
circ1.setOutline(dark_red)
circ2.setOutline(dark_red)
time.sleep(1)
card.setBackground(dark_red)
time.sleep(0.5)
big_poly.setFill(grey_blue)
poly2.setFill(grey_blue)
circ1.setFill(grey_blue)
circ2.setFill(grey_blue)

for i in range(5):
    time.sleep(0.1)
    circ3.setOutline(goldenrod)
    time.sleep(0.1)
    circ3.setOutline(dark_red)
time.sleep(0.5)
circ3.setOutline(alice_blue)
big_poly.setOutline(alice_blue)
poly2.setOutline(alice_blue)
circ1.setOutline(alice_blue)
circ2.setOutline(alice_blue)
star.draw(card)

top_txt.setTextColor(alice_blue)
bottom_txt.setTextColor(alice_blue)

time.sleep(0.5)
top_txt.setText("Happy Valentines")
bottom_txt.setText("Would you be")
time.sleep(0.5)
top_txt.setText("!!!")
bottom_txt.setText("Would")
time.sleep(0.5)
bottom_txt.setText("!!!")
time.sleep(0.5)
top_txt.setText("Happy")
bottom_txt.setText("Get")
time.sleep(0.5)
top_txt.setText("Happy Halloween!")
bottom_txt.setText("Get Ghouled!")
# for i in range(5):
    # point = card.getMouse()
    # x = point.getX()
    # y = point.getY()

    # pointt = Point(x, y)
    # pointt.draw(card)
    # print(pointt)
# close

end_txt = bottom_txt.clone()
end_txt.move(0, 25)
end_txt.setText("Click anywhere to close.")
end_txt.setTextColor(light_cyan)
end_txt.draw(card)

card.getMouse()
card.close()
