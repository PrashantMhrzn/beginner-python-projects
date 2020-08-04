
import random


def roll():
    for i in range(1,turn+1):
        roll = random.randint(1,sides)
        counter.append(roll)
        print(f'{i} roll: {roll}')
        

def track():
    for i in range(120):
        if counter.count(i)>=1:
            print(f'{i} came {counter.count(i)} times')


choices='''
1. Enter the program
2. Exit
Enter your choice:
'''

try:
    usr_inp = int(input(choices))
    while usr_inp != 2:
        if usr_inp == 1:
            sides=int(input('Enter the number of sides: '))
            if sides > 120:
                print('Max limit for sides of a dice is 120!!')
                exit()
            turn=int(input('Enter how many times should the dice roll: '))
            counter=[]
            roll()
            track()
        else:
            print('Invalid option!')
        usr_inp = int(input(choices))
except ValueError:
    print('Invalid Input! Enter a number!!')