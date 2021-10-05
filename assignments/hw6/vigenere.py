"""
William McClain
vigenere.py

Problem: Create a program that implements the vigenere cypher, getting an input
from the user and giving an output that uses the cypher given a key also input by
the user. The program should have a gui.

Affirmation: I affirm that the code bellow is all my own work.
"""
from graphics import GraphWin, Text, Entry, Point

def main():
    height = 500
    width = 600
    gui = GraphWin('Vigenere', width, height)
    inst_pt = Point(width / 2, height - 50)
    in_text_pt = inst_pt.clone()
    in_text_pt.move(0, -25)
    instructions = Text(inst_pt, 'Stop')
    instructions.draw(gui)
    input_text = Entry(in_text_pt, 5)
    input_text.draw(gui)

    gui.getMouse()
if __name__ == '__main__':
    main()
