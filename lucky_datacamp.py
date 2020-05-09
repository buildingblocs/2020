import csv
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
                # includes [name, school, email]
                participants.append([row[1], row[2], row[3]])
    num_participants = len(participants)
    return (participants, num_participants)


def winner(participants, winner_num):
    """Choose Winner"""
    rng.shuffle(participants)
    winner_list = []
    used_email = set()  # Set

    # boundary check, participants > prizes
    if num_participants > winner_num:
        while len(winner_list) != winner_num:
            index = rng.randint(0, num_participants - 1)
            if not (participants[index][1] in used_email):  # prevent repeats
                winner_list.append(participants[index])
                used_email.add(participants[index][1])

    else:  # participants < prizes
        winner_list = participants
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
        [4]: Read and print weighted current candidates (not random)
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
        participants, num_participants = read(
            csv_path)  # reads file and unpack tuple
        winner_list = winner(participants, winner_num)  # returns winner list
        display(winner_list, prizes)  # outputs
    elif menu_option == 2:
        print("Drawing Winner with Weighted chances")
        participants, num_participants = read_weighted(
            csv_path)  # reads file and unpack tuple
        winner_list = winner(participants, winner_num)  # returns winner list
        display(winner_list, prizes)  # outputs
    elif menu_option == 3:
        csv_path = input("Enter new CSV path: ")
    elif menu_option == 4:
        participants, num_participants = read_weighted(
            csv_path)  # reads file and unpack tuple
        names = [element[0] for element in participants]
        pp.pprint(names)
    else:
        print("Exiting...")
        exit()
