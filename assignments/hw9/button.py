"""
William McClain
button.py
Problem: Create a button class for the ThreeDoorGame.py function
Affirmation: I affirm that this is all my own work.
"""
from graphics import Rectangle, Point, Text, color_rgb, GraphWin


class Button:
    def __init__(self, Rectangle_shape, String_label):
        """

        """
        self.Rectangle_shape = Rectangle_shape
        self.String_label = String_label

    def draw(self, Window):
        """

        """
        text_center = self.Rectangle_shape.getCenter()
        self.Rectangle_shape.draw(Window)
        Text(text_center, self.String_label).draw(Window)


    # def undraw(self):


    def set_color(self, rgb_value):
        """

        """
        self.Rectangle_shape.setFill(color_rgb(rgb_value))


    def set_label(self, new_string):
        """

        """
        self.String_label = new_string

    def get_label(self):
        """

        """
        return self.String_label

    def is_clicked(self, point):
        """

        """
        