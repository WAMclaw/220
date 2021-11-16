from random import randint  # (should be at tip top, just for me to remember)
"""
Name: William McClain
hangman.py
Problem: make a functioning hangman game
Affirmation: I affirm that the following code is all my own work with help from the TA and LT.
"""


def input_list(in_file):
    word_file = open(in_file, 'r')
    words = []
    for line in word_file:
        word = line.strip('\n')
        word.lower()
        words.append(word)
    word_file.close()
    return words


def choose_word(word_list):
    leng_list = len(word_list)
    return word_list[randint(0, leng_list-1)].lower()


def make_word_into_list(word):
    game_word_list = []
    for i in len(word):
        game_word_list.append(word(i))


def hidden_stat(in_stat):
    hid_sent = in_stat.lower()
    # hid = hid_sent.split()
    hid2 = '_' * len(hid_sent.lower())
    # for i in range(len(hid)):
    #     guess = '_' * len(hid[i])
    #     hid2.append(guess)
    return hid2


def check_if_guessed(guess):
    return guess.find('_') > 0


# def game_hm(word, guess, letter):
#     for i in range(word.count(letter)):
#         num = int(word.find(letter))
#         guess[num] = letter

def main():
    word_list_game = input_list('words_for_hanging.txt')
    print(word_list_game)
    game_word = choose_word(word_list_game)
    print(game_word)
    hidden = hidden_stat(game_word)
    print(hidden)
    hidden2 = []
    for i in range(len(hidden)):
        hidden2.append(i)
    # print(hidden2)
    # add other function calls here
    count = 7
    while count > 0:
        letter = input("Let's play hang man. Guess a letter: ").lower()
        print(letter)
        for num in range(game_word.count(letter)):
            print(game_word.index(letter))
            game_word = game_word.replace(letter,'1')
            print(game_word)
            print(hidden2)
        for item in hidden:
            if check_if_guessed(item) == True:
                count = -1
        print(hidden2)
        count = count - 1
    # for item in hidden:
    #     print(check_if_guessed(item))


    pass


main()
