"""
Name: William McClain
lab6.py
I affirm that all of this code is my own work with help from the TA and LT.
"""
def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input('Write the first and last name with a space in between: ')
    name_list = name.split()
    rev_name = name_list[-1] + ', ' + name_list[0]
    print(rev_name)


def company_name():
    """
    take a company web domain and just get the name
    """
    comp_name = input('Enter a three-part web domain. [www.example.com]: ')
    comp_list = comp_name.split('.')
    company = comp_list[1]
    print(str(company))


def initials():
    """
    get the initials of multiple names, first and last
    """
    class_num = eval(input('How many student names will be entered: '))
    number = 0
    for num in range(class_num):
        number = number + 1
        inst = 'Enter the name of student ' + str(number) + ": "
        first = input(inst)
        last_inst = 'Enter ' + first + "'s last name: "
        last = input(last_inst)
        first_init = str(first[0])
        last_init = str(last[0])
        init = first + "'s initials are " + first_init[0] + last_init[0]
        print(init)


def names():
    """
    list the names of multiple people entered at once
    """
    print("List people's names separated by a comma and a space [first_name last_name, first_name last_name]")
    namen = input("First and last names only: ")
    list_names = namen.split(', ')
    #num_nams = len(list_names)
    print("The initials are", end=' ')
    for name_num in list_names:
        name = name_num.split(' ')
        first = name[0]
        last = name[1]
        first_init = str(first[0])
        last_init = str(last[0])
        init = first_init[0] + last_init[0]
        print(init, end=', ')
    print()


def thirds():
    """
    get every third character of a sentence
    """
    num_sent = eval(input('How many sentences will be input: '))

    for numb in range(num_sent):
        inst = 'Enter the sentence ' + str(numb+1) + ': '
        user_text = input(inst)
        length = len(inst)
        print(str(length))
        ph = 0
        for number in range(1, length//3):
            ph = (number * 3) - 1
            char = user_text[ph]
            print(char, end='')
        print()


def word_average():
    """
    get the letter average of words
    """
    sent = input('Enter a sentence to get average letter count per word: ')
    words = sent.split(' ')
    sum = 0
    number = len(words)
    for word in words:
        length = len(word)
        sum = sum + length
    avg_letter = sum / number
    print(str(avg_letter))


def pig_latin():
    """
    make a function that can generate pig latin from a given sentence
    """
    sent = input('Enter a sentence ot be turned into pig latin: ')
    words = sent.split(' ')
    for word in words:
        first = str(word[0]).lower()
        mid = str(word[1:])
        pig = mid + first + 'ay'
        print(pig, end=' ')


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()


main()
