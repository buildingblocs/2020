# this is the file for lucky draw
import random

def showprizes():
    input('Prizes...')
    print('1st:', prizes[0])
    print('2nd:', prizes[1])
    print('3rd:', prizes[2])
    print('4th:', prizes[3])
    print('5th:', prizes[4])
    print()
    
def getallnames():
    with open('BuildingBloCS 2019 Conference Registration (Responses) - Form Responses 1.csv', 'r') as infile:
        lines = infile.readlines()
    # remove first line as it is the heading
    lines.pop(0)
    for line in lines:
        line = line.strip().split(',')
# when teachers are not eligible for the lucky draw
##        # add name into array names if person is not a teacher
##        # and sch into school array
##        if 'Teacher' not in line:
##            names.append(line[1].strip())
##            school.append(line[3].strip())
        names.append(line[1].strip())
        school.append(line[3].strip())
    #remove name repeats if school is same
    for i in range(len(names)):
        # check if index exceeds length of array names,
        # since some items are removed from array,
        # i will run past the length
        if i > len(names)-1:
            break
        # curr and repeat are indexes of where the names are
        # curr is a constant index where the current name is 
        name = names[i]
        curr = i
        repeat = -2
        # when there are more than 1 of same name in array
        while names.count(name) > 1:
            for j in range(curr+1, len(names)):
                if names[j] == name:
                    repeat = j
                    break
                repeat = -1
            # end case: no more repeats behind 
            if repeat == -1:
                break
            # shift back index to the original one
            curr = i
            if school[curr] == school[repeat]:
                school.pop(repeat)
                names.pop(repeat)
            else:
                # end case: looked through every item
                if repeat == len(names)-1:
                    break
                else:
                    # temporarily shift index to find the next
                    # repeated name 
                    curr = repeat

def getlucky():
    if len(names) < 5:
        print('Not enough participants for luckydraw!')
    else:
        # randomises 5 winners
        for i in range(5):
            winnerindex = random.randint(0, len(names)-1)
            winner = names[winnerindex]
            winners.append(winner)
            winners.append(school[winnerindex])
            # remove from arrays so they will not be repeated
            school.pop(winnerindex)
            names.pop(winnerindex)
        input()
        input('Show the winners!')
        print('5th:', winners[8]+',', winners[9]+',', prizes[4])
        input('Next winner is...')
        print('4th:', winners[6]+',', winners[7]+',', prizes[3])
        input('Next winner is...')
        print('3rd:', winners[4]+',', winners[5]+',', prizes[2])
        input('Next winner is...')
        print('2nd:', winners[2]+',', winners[3]+',', prizes[1])
        input('Next winner is...')
        print('1st:', winners[0]+',', winners[1]+',', prizes[0])
        print()


def displayresults():
    # display winners
    input()
    input('Results...')
    print(week, 'week, lucky draw!')
    print('1st:', winners[0]+',', winners[1]+',', prizes[0])
    print('2nd:', winners[2]+',', winners[3]+',', prizes[1])
    print('3rd:', winners[4]+',', winners[5]+',', prizes[2])
    print('4th:', winners[6]+',', winners[7]+',', prizes[3])
    print('5th:', winners[8]+',', winners[9]+',', prizes[4])
    print()
    print('Congratulations!!')

# function for when winners can only win once in the whole lucky draw
##def pastwinners():
##    # using a+ to create the textfile if it does not exist 
##    with open('winners.txt', 'a+') as infile:
##        infile.seek(0)
##        lines = infile.readlines()
##    for line in lines:
##        line = line.strip()
##        # check for empty lines/line without winners name
##        if 'week' not in line and line:
##            details = line.split(':')[1].strip()
##            name = details.split(',')[0]
##            school.pop(names.index(name))
##            names.remove(name)

def recordwinners():
    # append to textfile for future references 
    with open('winners.txt', 'a') as outfile:
        output = week+' week\n'
        outfile.write(output)
        output = '1st: '+winners[0]+', '+winners[1]+', '+prizes[0]+'\n'
        outfile.write(output)
        output = '2nd: '+winners[2]+', '+winners[3]+', '+prizes[1]+'\n'
        outfile.write(output)
        output = '3rd: '+winners[4]+', '+winners[5]+', '+prizes[2]+'\n'
        outfile.write(output)
        output = '4th: '+winners[6]+', '+winners[7]+', '+prizes[3]+'\n'
        outfile.write(output)
        output = '5th: '+winners[8]+', '+winners[9]+', '+prizes[4]+'\n'
        outfile.write(output)
        outfile.write('\n')

#main
# this variable changes each week
week = 'First'
names = []
school = []
winners = []
prizes = ['Google Chromecast', '2 "Endgame" tickets', '2018 Fossasia shirt',\
          'Fidget Cube', 'Packet of post-its']

showprizes()
getallnames()
#pastwinners()
getlucky()
recordwinners()
displayresults()
