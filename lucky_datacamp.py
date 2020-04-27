import csv
import random
import time

# Configuration
winner_num = 3  # Number of winners
prizes = ['t-shirt', 't-shirt', 't-shirt']  # top-prize first
csv_path = "lucky_draw2.csv"  # Path of CSV File


def read(csv_path):
    """Convert CSV to lists names, emails, schools and return lists"""
    i = 0
    names, schools, emails = [], [], []
    with open(csv_path, 'r') as file:
        lines = csv.reader(file)
        for row in lines:  # row: list
            if i != 0:  # takes away headers
                names += [row[1]]
                emails += [row[2]]
                schools += [row[3]]
            i += 1
    num_participants = len(names)
    return (names, emails, schools, num_participants)


def winner(names, winner_num):
    """Choose Winner"""
    winner_list = []
    used_email = ''
    if num_participants > winner_num:  # boundary check, participants > prizes
        while len(winner_list) != winner_num:
            index = random.randint(0, num_participants-1)
            if not (emails[index] in used_email):  # prevent repeats
                winner_list += [[names[index], emails[index], schools[index]]]
                used_email += emails[index]

    else:  # participants < prizes
        for index in range(0, num_participants):
            winner_list += [[names[index], emails[index], schools[index]]]
        random.shuffle(winner_list)  # changes the order of names -> random
    return winner_list


def display(winner_list, prizes):
    """Display Winner"""
    print('Here are the results!')
    count = len(winner_list)
    for element in winner_list:
        print(
            f'In the {count} place, we have {element[0]} from {element[2]} winning {prizes[count-1]}')
        count -= 1
        # time.sleep(2) #automatic


# main
(names, emails, schools, num_participants) = read(
    csv_path)  # reads file and unpack tuple
winner_list = winner(names, winner_num)  # returns winner list
display(winner_list, prizes)  # outputs
