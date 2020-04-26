import csv, random, time
names, schools, emails = [], [], []
num_participants = 0
winner_list = []
winner_num = 3 #number of winners
prizes = ['t-shirt', 't-shirt', 't-shirt'] #top-prize first

def read():
    global names
    global schools
    global emails
    global num_participants
    i = 0
    with open('lucky_draw3.csv', 'r') as file:
        lines = csv.reader(file)
        for row in lines:#row: list
            if i != 0: #takes away headers
                names += [row[1]]
                emails += [row[2]]
                schools += [row[3]]            
            i += 1
            
    num_participants = len(names)

def winner(names):
    global winner_num
    global winner_list
    used_email = ''
    if num_participants > winner_num: #boundary check, participants > prizes
        while len(winner_list) != winner_num:
            index = random.randint(0, num_participants-1)
            if not (emails[index] in used_email): #prevent repeats
                winner_list += [[names[index], emails[index], schools[index]]]
                used_email += emails[index]
                
    else: #participants < prizes
        for index in range (0, num_participants):
            winner_list += [[names[index], emails[index], schools[index]]]
        random.shuffle(winner_list) #changes the order of names -> random

    return winner_list

def display():
    print('Here are the results!')
    count = len(winner_list)
    for element in winner_list:
        print('In the {} place, we have {} from {} winning {}'.format(count, element[0], element[2], prizes[count-1]))
        count -= 1
        #time.sleep(2) #automatic
        input()
            
        

#main
read() #reads file
winner(names) #returns winner list
display() #outputs
