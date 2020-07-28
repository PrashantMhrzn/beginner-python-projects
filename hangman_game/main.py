import random


words = ['airplane', 'elephant', 'dock', 'army',
         'iridocyclitis', 'memphis', 'jesus', 'brandy', 'beer', 'london', 'consanguineous', 'xenotransplantation']
ans = random.choice(words)


guessed = []
wrong = []
tries = len(ans)-1
print('*****Welcome to hangman!!!*****')
while tries > 0:
    brk = ''
    for letter in ans:
        if letter in guessed:
            brk += letter
        else:
            brk += '_'
    print(brk)
    print(f'you have {tries} tries left')
    if brk == ans:
        print('YOU WON!!!')
        break

    usr_inp = input('guess a letter: ').lower()
    print('')
    if usr_inp == 'exit':
        break

    if usr_inp in guessed or usr_inp in wrong:
        print('already guessed!!')
        tries -= 1
    elif usr_inp in ans:
        print('you guessed the right letter!')
        guessed.append(usr_inp)
    else:
        print('you guessed the wrong letter!')
        wrong.append(usr_inp)
        tries -= 1

if tries:
    print(f'you guessed the answer {ans}')
else:
    print('YOU LOST!!!')
    print(f'you didnt guess the answer {ans}')

print('*****Thanks for playing the game!!!*****')
