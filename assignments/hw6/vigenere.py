"""
William McClain
vigenere.py

Problem: Create a program that implements the vigenere cypher, getting an input
from the user and giving an output that uses the cypher given a key also input by
the user. The program should have a gui.

Affirmation: I affirm that the code bellow is all my own work.
"""
from graphics import * # GraphWin, Text, Entry, Point, Rectangle


def code(message, keyword):
    input_text = message
    input_key = keyword

    input_text = input_text.upper()
    input_key = input_key.upper()
    text_list = []
    text_list[:0] = input_text.replace(" ", "")
    key_list = []
    key_list[:0] = input_key.replace(" ", "")
    i = 0
    n = len(key_list)
    strntxt = ''

    print(text_list)
    print(key_list)
    for val in text_list:
        num = ord(val)
        knum = ord(key_list[((i + n) % n)])
        num_shift = knum - 65
        new = num + num_shift
        if new > 90:
            ###
            new = new - 26
        # these two if statements take the loop of the alphabet into account and if spaces are in the text
        new_ch = chr(new)
        text_list[i] = new_ch
        strntxt = strntxt + new_ch
        # print(text_list[i], end='')
        i = i + 1

    return strntxt

def main():
    height = 300
    width = 300
    gui = GraphWin('Vigenere', width, height)
    inst_pt = Point(width / 2, height / 5)
    in_text_pt = inst_pt.clone()
    in_text_pt.move(0, 25)
    inst_pt_2 = in_text_pt.clone()
    inst_pt_2.move(0, 50)
    in_key_pt = inst_pt_2.clone()
    in_key_pt.move(0, 25)
    out_text_pt = in_key_pt.clone()
    out_text_pt.move(0, 50)
    fin_inst_pt = out_text_pt.clone()
    fin_inst_pt.move(0, 50)
    fin_x = fin_inst_pt.getX()
    fin_y = fin_inst_pt.getY()
    button = Rectangle(Point(fin_x - 75, fin_y - 20), Point(fin_x + 75, fin_y + 20))
    button.draw(gui)

    inst1 = Text(inst_pt, 'Enter your text below')
    inst2 = Text(inst_pt_2, 'Enter your key below')
    inst3 = Text(fin_inst_pt, 'Click to Encode')
    out = Text(out_text_pt, '[Message]')
    inst1.draw(gui)
    inst2.draw(gui)
    inst3.draw(gui)
    out.draw(gui)
    in_text_entry = Entry(in_text_pt, 10)
    in_key_entry = Entry(in_key_pt, 6)
    in_text_entry.draw(gui)
    in_key_entry.draw(gui)
    gui.getMouse()
    input_text = in_text_entry.getText()
    input_key = in_key_entry.getText()

    # lists set up
    """
    alpha = ' , a, b, c, d, e, f, g, h, i, j, k, l, m , n, o, p, q, r, s, t, u, v, w, x, y, z'
    alphabet = alpha.split(', ')
    num_an = [0] * 26
    for num in range(len(num_an)):
        num_an[num] = num + 1
    text_list = []
    text_list[:0] = input_text
    key_list = []
    key_list[:0] = input_key
    alpha_text_list = []

    print(key_list)
    print(text_list)
    alpha_num_ph = 0
    for var in range(len(text_list)):
        let = text_list[var]
        print(let)
        num = alphabet.index(let)
        alpha_text_list[alpha_num_ph] = num
        alpha_num_ph = alpha_num_ph + 1

    print(alpha_text_list)
        # need to add a replace statement for the new number statement text

    # need to replace these with numbers to make it simpler
    # need to add a lower case defaulter into code for the inputs
    # don't forget to add the modulo fix for the alphabets
    for var in range(len(text_list)):
        alpha_text_list[var:0] = key_list[(var + len(key_list)) % len(key_list)]
    """

    input_text = input_text.upper()
    input_key = input_key.upper()
    text_list = []
    text_list[:0] = input_text.replace(" ", "")
    key_list = []
    key_list[:0] = input_key.replace(" ", "")
    i = 0
    n = len(key_list)
    strntxt = ''

    print(text_list)
    print(key_list)
    for val in text_list:
        num = ord(val)
        knum = ord(key_list[((i + n) % n)])
        num_shift = knum - 65
        new = num + num_shift
        if new > 90:
            ###
            new = new - 26
        # these two if statements take the loop of the alphabet into account and if spaces are in the text
        new_ch = chr(new)
        text_list[i] = new_ch
        strntxt = strntxt + new_ch
        # print(text_list[i], end='')
        i = i + 1

    # gives final coded message and changes instruction button
    out.setText(strntxt)
    # out.setText('[Code]')
    inst3.setText('Click to Close')
    gui.getMouse()


if __name__ == '__main__':
    main()
