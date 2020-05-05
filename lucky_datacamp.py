import csv
import time
import secrets
import pprint
rng = secrets.SystemRandom()  # Same interface as random module
pp = pprint.PrettyPrinter()

# Configuration
winner_num = 3  # Number of winners
prizes = ['t-shirt', 't-shirt', 't-shirt']  # top-prize first
# Path of CSV File
csv_path = r"lucky_draw2.csv"


def read(csv_path):
    """NON WEIGHTED Convert CSV to lists names, emails, schools and return lists"""
    names, schools, emails = [], [], []
    with open(csv_path, 'r') as file:
        lines = csv.reader(file)
        next(lines)  # This skips the first row of the CSV file
        for row in lines:  # row: list
            names.append(row[1])
            emails.append(row[2])
            schools.append(row[3])
    num_participants = len(names)
    return (names, emails, schools, num_participants)


def read_weighted(csv_path):
    """WEIGHTED Convert CSV to lists names, emails, schools and return lists"""
    names, schools, emails = [], [], []
    with open(csv_path, 'r') as file:
        lines = csv.reader(file)
        next(lines)  # This skips the first row of the CSV file
        for row in lines:  # row: list
            try:
                chance = int(row[4])
            except:
                chance = 1  # Default chance is 1
            for _ in range(chance):
                names.append(row[1])
                emails.append(row[2])
                schools.append(row[3])
    num_participants = len(names)
    return (names, emails, schools, num_participants)


def winner(names, winner_num):
    """Choose Winner"""
    winner_list = []
    used_email = set()  # Set

    # boundary check, participants > prizes
    if num_participants > winner_num:
        while len(winner_list) != winner_num:
            index = rng.randint(0, num_participants - 1)
            if not (emails[index] in used_email):  # prevent repeats
                winner_list.append(
                    [names[index], emails[index], schools[index]])
                used_email.add(emails[index])
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


# Menu
while True:
    try:
        print(
            """
        Welcome to BuildingBloCS Lucky draw program!
        Menu:
        [1]: Draw winner
        [2]: Draw winner with weighted chances
        [3]: Set CSV file path
        [4]: Read and print weighted current candidates
        [5]: Exit
        """
        )
        menu_option = int(input("Option: "))
        if not 1 <= menu_option <= 5:
            raise Exception("Invalid Option")
    except Exception as e:
        print("Invalid Input")
        continue
    if menu_option == 1:
        print("Drawing Winner")
        (names, emails, schools, num_participants) = read(
            csv_path)  # reads file and unpack tuple
        winner_list = winner(names, winner_num)  # returns winner list
        display(winner_list, prizes)  # outputs
    elif menu_option == 2:
        print("Drawing Winner with Weighted chances")
        (names, emails, schools, num_participants) = read_weighted(
            csv_path)  # reads file and unpack tuple
        winner_list = winner(names, winner_num)  # returns winner list
        display(winner_list, prizes)  # outputs
    elif menu_option == 3:
        csv_path = input("Enter new CSV path: ")
    elif menu_option == 4:
        (names, emails, schools, num_participants) = read_weighted(
            csv_path)  # reads file and unpack tuple
        pp.pprint(names)
    else:
        print("Exiting...")
        exit()
