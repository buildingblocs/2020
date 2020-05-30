# Import Prerequisite modules
import csv
import secrets
import pprint

# The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as
# passwords, account authentication, security tokens, and related secrets.
#
# In particularly, secrets should be used in preference to the default pseudo-random number generator in the random module,
# which is designed for modelling and simulation, not security or cryptography.

rng = secrets.SystemRandom()
# Same interface as random module
# A class for generating random numbers using the highest-quality sources provided by the operating system.
# Essentially more random than the random module

pp = pprint.PrettyPrinter()

# Configuration
winner_num = 5  # Number of winners

# Top-prize first
prizes = ['USB wrist band',
          'USB wrist band',
          'USB wrist band',
          'USB wrist band',
          'USB wrist band']
# Path of CSV File
csv_path = 'Intro_js.csv'

# Globals Vars
used_email = set()
# Set
# A set is a collection which is unordered and unindexed. Set in Python is a data structure equivalent to sets in mathematics.


def read(csv_path):
    """NON WEIGHTED Convert CSV to lists names, emails, schools and return lists"""
    participants = []
    with open(csv_path, 'r') as file:
        lines = csv.reader(file)
        next(lines)  # This skips the first row of the CSV file
        for row in lines:  # row: list
            # includes [name, school, email]
            participants.append([row[1], row[2], row[3]])
    num_participants = len(participants)
    return (participants, num_participants)


def read_weighted(csv_path):
    """WEIGHTED Convert CSV to lists names, emails, schools and return lists"""
    participants = []
    with open(csv_path, 'r') as file:
        lines = csv.reader(file)
        next(lines)  # This skips the first row of the CSV file
        for row in lines:  # row: list
            try:
                chance = int(row[4])
            except:
                chance = 1  # Default chance is 1
            for _ in range(chance):
                # includes [name, email, school]
                participants.append([row[1], row[2], row[3]])
    num_participants = len(participants)
    return (participants, num_participants)


def winner(participants, winner_num, num_participants):
    """Choose Winner"""
    rng.shuffle(participants)
    winner_list = []
    global used_email
    # Boundary check
    # participants > prizes
    if num_participants > winner_num:
        while len(winner_list) != winner_num:
            index = rng.randint(0, num_participants - 1)
            if not (participants[index][1] in used_email):  # prevent repeats
                winner_list.append(participants[index])
                used_email.add(participants[index][1])

    # participants <= prizes
    elif num_participants <= winner_num:
        winner_list = participants
    return winner_list


def redraw(participants, num_participants):
    while True:
        index = rng.randint(0, num_participants - 1)
        if not (participants[index][1] in used_email):
            used_email.add(participants[index][1])
            return participants[index]


def display(winner_list, prizes, participants, num_participants):
    """Display Winner"""
    print('Here are the results!')
    count = len(winner_list)
    for element in winner_list:
        if count == 1:
            print(
                f'In the 1st place, we have {element[0]} from {element[2]} winning {prizes[count-1]}')
        elif count == 2:
            print(
                f'In the 2nd place, we have {element[0]} from {element[2]} winning {prizes[count-1]}')
        else:
            print(
                f'In the {count}th place, we have {element[0]} from {element[2]} winning {prizes[count-1]}')
        while True:
            x = input("Redraw? [Y/N] [YES/NO] [DEFAULT:N]: ")
            if x.upper() == "Y" or x.upper() == "YES":
                element = redraw(participants, num_participants)
                if count == 1:
                    print(
                        f'In the 1st place, we have {element[0]} from {element[2]} winning {prizes[count-1]}')
                elif count == 2:
                    print(
                        f'In the 2nd place, we have {element[0]} from {element[2]} winning {prizes[count-1]}')
                else:
                    print(
                        f'In the {count}th place, we have {element[0]} from {element[2]} winning {prizes[count-1]}')
            else:
                break
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
        [4]: Read and print weighted current candidates (not random)
        [5]: Print Prizes in descending order
        [6]: Exit
        """
        )
        # Input Sanity Check
        menu_option = int(input("Option: "))
        if not 1 <= menu_option <= 6:
            raise Exception("Invalid Option")

    except Exception as e:
        print("Invalid Input")
        continue
    if menu_option == 1:
        print("Drawing Winner")
        # reads file and unpack tuple
        participants, num_participants = read(
            csv_path)
        # returns winner list
        winner_list = winner(participants, winner_num,
                             num_participants)
        # outputs
        display(winner_list, prizes, participants, num_participants)
    elif menu_option == 2:
        print("Drawing Winner with Weighted chances")
        # reads file and unpack tuple
        participants, num_participants = read_weighted(
            csv_path)
        # returns winner list
        winner_list = winner(participants, winner_num,
                             num_participants)
        # outputs
        display(winner_list, prizes, participants, num_participants)
    elif menu_option == 3:
        csv_path = input("Enter new CSV path: ")
    elif menu_option == 4:
        participants, num_participants = read_weighted(
            csv_path)  # reads file and unpack tuple
        names = [element[0] for element in participants]
        pp.pprint(names)
    elif menu_option == 5:
        print("The Prizes are: ")
        pp.pprint(prizes)
    else:
        print("Exiting...")
        exit()
    input()
