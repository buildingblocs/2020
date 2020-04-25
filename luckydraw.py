#buildingblocs lucky draw
import random,csv

def getnames():
    i = 0
    with open("lucky_draw.csv","r") as file:
        lines = csv.reader(file)
        for line in lines:
            if i != 0:
                all_names.append(line[1])
                all_schools.append(line[3])
            i += 1
    return len(all_names)
            
def draw(number_of_winners,number_of_participants):
    if number_of_participants >= number_of_winners:
        used = []
        for i in range(number_of_winners):
            lucky_index = random.randint(0,len(all_names)-1)
            while lucky_index in used:
                lucky_index = random.randint(0,len(all_names)-1)
            used.append(lucky_index)
            winner = all_names[lucky_index],all_schools[lucky_index]
            winners.append(winner)
    else:
        random.shuffle(prizes)
        for i in range(number_of_participants):
            print("{} has won {}".format(all_names[0],prizes(i)))


def display(number_of_winners):
    print("Here are the results!\n")
    for i in range(number_of_winners, 0, -1):
        print(f'In the {i} place, we have {winners[i-1][0]} from {winners[i-1][1]} winning')
        input()
        print(f"{prizes[i-1]}")
        input()
        
    
#main

all_names = []
all_schools = []
number_of_participants = getnames()
winners = []
prizes = ["mystery prize","hand sanitiser x 1","face masks x 2","alcohol swabs x 4","toilet paper x 8"]
number_of_winners = 5
draw(number_of_winners,number_of_participants)
display(number_of_winners)