"""
Name: William McClain
lab8.py
Problem:
Affirmation: I affirm that everything in this code is my own work with the help of the TA and LT
"""
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    in_txt = open(in_file_name, 'r')
    out_txt = open(out_file_name, 'w')
    fin_list = []
    for line in in_txt:
        a_line = line.strip('\n')
        a_list = a_line.rsplit()
        fin_list = fin_list + a_list
    for num in range(len(fin_list)):
        num_word_txt = str(num + 1) + ' ' + fin_list[num] + '\n'
        out_txt.write(num_word_txt)
    in_txt.close()
    out_txt.close()


def hourly_wages(in_file_name, out_file_name):
    in_txt = open(in_file_name, 'r')
    out_txt = open(out_file_name, 'w')

    fin_list = []
    for line in in_txt:
        a_line = line.strip('\n')
        a_list = a_line.rsplit()
        fin_list = fin_list + a_list
    for num in range(int(len(fin_list) / 4)):
        new_hourly = float(fin_list[num * 4 + 2]) + 1.65
        weeks_pay = round(new_hourly * float(fin_list[num * 4 + 3]), 2)
        new_wage_txt = fin_list[num * 4] + ' ' + fin_list[num * 4 + 1] + ' ' + str(weeks_pay) + '\n'
        out_txt.write(new_wage_txt)
    in_txt.close()
    out_txt.close()


def calc_check_sum(isbn):
    position = 10
    isbn_tot = 0
    for number in isbn:
        mul = int(number) * position
        isbn_tot = isbn_tot + mul
        position = position - 1
    isbn_check = isbn_tot % 11
    print(isbn_check)


def send_message(file, friend):
    in_txt = open(file, 'r')
    out_txt = open(friend, 'w')

    for line in in_txt:
        txt = line.strip('\n')
        out_txt.write(txt)
    in_txt.close()
    out_txt.close()


"""
def encode(text_in, key):
    text_list = []
    key_in = key
    text_list[:0] = text_in
    i = 0
    encode_txt = ''
    for val in text_list:
        num = ord(val)
        num = num + key_in
        # these two if statements take the loop of the alphabet into account and if spaces are in the text
        if num > 122:
            num = num - 26
        if num == key_in + 32:
            num = 32
        new_ch = chr(num)
        text_list[i] = new_ch
        print(text_list[i], end='')
        i = i + 1
        encode_txt = encode_txt + new_ch
    return encode_txt
"""


def send_safe_message(file, friend, key):
    in_txt = open(file, 'r')
    in_key = open(key, 'r')
    out_txt = open(friend, 'w')

    fin_str = ''
    for line in in_txt:
        a_line = line.strip('\n')
        fin_str = fin_str + a_line
    for key_line in in_key:
        a_line = key_line.strip('\n')
        key = a_line

    encoded_msg = encode(fin_str, key)
    out_txt.write(encoded_msg)

    in_txt.close()
    out_txt.close()


def send_uncrackable_message(file, friend, pad):
    in_txt = open(file, 'r')
    in_pad = open(pad, 'r')
    out_txt = open(friend, 'w')

    fin_str = ''
    fin_list = []
    for line in in_txt:
        a_line = line.strip('\n')
        a_list = a_line.rsplit()
        fin_list = fin_list + a_list
        for item in fin_list:
            fin_str = fin_str + item
    for pad_line in in_pad:
        a_line = pad_line.strip('\n')
        key = a_line

    encoded_message = encode_better(fin_str, key)
    out_txt.write(encoded_message)

    in_txt.close()
    out_txt.close()


def main():
    # number_words('Walrus.txt', 'Bilo.txt')
    # hourly_wages('hourly_wages.txt', 'new_weeks_wages.txt')
    # calc_check_sum('0072946520')
    # send_message('message.txt', 'bob.txt')
    # send_safe_message('secret_message.txt', 'encoded_msg.txt', 3)
    send_uncrackable_message('safest_message.txt', 'uncracked_msg.txt', 'pad.txt')
    pass


main()
