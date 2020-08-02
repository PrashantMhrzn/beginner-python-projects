import random
from time import sleep


def magic():
    responses = ['As I see it, yes.', 'Most likely.',
                 'My reply is no.', 'Without a doubt.', 'Yes – definitely.', ]
    response = random.choice(responses)
    print(response)


print('-------Hello!!! I\'m The Magic 8 Ball!!-------')
while True:
    quest = input('Enter any question: ')
    print('hmmmm....wait a sec I\'m thinking')
    sleep(2)
    magic()
    cont = input('Wish to conyinue?(y/n)').lower()
    if cont == 'y':
        continue
    elif cont == 'n':
        print('I hope you still like me...XD')
        break
    else:
        print("Hey dumbo!! Enter 'y' or 'n' only!! Restarting the program...")
        continue
print('The Magic 8 Ball Goes To Sleep.. zzzz...')
