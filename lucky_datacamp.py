import csv
import time
import secrets
rng = secrets.SystemRandom()  # Same interface as random module

# Configuration
winner_num = 3  # Number of winners
prizes = ['t-shirt', 't-shirt', 't-shirt']  # top-prize first
# Path of CSV File
csv_path = r"lucky_draw2.csv"


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
    used_email = []

    # boundary check, participants > prizes
    if num_participants > winner_num:
        while len(winner_list) != winner_num:
            index = rng.randint(0, num_participants - 1)
            if not (emails[index] in used_email):  # prevent repeats
                winner_list.append(
                    [names[index], emails[index], schools[index]])
                used_email.append(emails[index])
    # participants < prizes
    else:
        for index in range(0, num_participants):
            winner_list += [[names[index], emails[index], schools[index]]]
        rng.shuffle(winner_list)  # changes the order of names -> random
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


(names, emails, schools, num_participants) = read(
    csv_path)  # reads file and unpack tuple
winner_list = winner(names, winner_num)  # returns winner list
display(winner_list, prizes)  # outputs
