"""
Name: William McClain
lab10.py
Problem: make a tic tac toe game in the terminal
Affirmation: I affirm that all code below is my own with the help of the TA and LT
"""


def list_a():
    listubt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return listubt


def ttt_board(into):
    list = into
    # print(list)
    top_left, top_mid, top_right = str(list[0]), str(list[1]), str(list[2])
    mid_left, true_mid, mid_right = str(list[3]), str(list[4]), str(list[5])
    bottom_left, bottom_mid, bottom_right = str(list[6]), str(list[7]), str(list[8])
    inner_line = '|'
    print(top_left, inner_line, top_mid, inner_line, top_right)
    print('----------')
    print(mid_left, inner_line, true_mid, inner_line, mid_right)
    print('----------')
    print(bottom_left, inner_line, bottom_mid, inner_line, bottom_right)


def move():
    choice = ''
    legal = is_legal(choice)
    while len(choice) != 2 or choice[1] != 'o' and choice[1] != 'x' or not choice[0].isnumeric() or int(choice[0]) < 1:
        choice = input('Enter your chosen placement [1-9] and character [X or O]:')
        choice = choice.lower()
    choice = choice.upper()
    return choice

#def is_legal(choice):
    #if

#def is_won():

def is_over(count, win):
    if count >= 9 or win:
        print('The game is over.')
        return True



def main():
    counter = 0
    listlow = list_a()
    ttt_board(listlow)
    over = False
    while not over:
        choice = move()
        space = eval(choice[0]) - 1
        character = choice[1]
        listlow[space] = character
        ttt_board(listlow)
        counter = counter+1
        win = False
        over = is_over(counter, win)
    pass


if __name__ == '__main__':
    main()
