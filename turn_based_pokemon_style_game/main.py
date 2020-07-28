import random
import time


class User():
    def scratch(self):
        return 10

    def fireball(self):
        return 30

    def heal(self):
        return 20


class Comp():
    def scratch(self):
        return 10

    def thunderbolt(self):
        return 30

    def heal(self):
        return 20


player = User()
comp = Comp()
player_health = 100
comp_health = 100
while True:
    print()
    print("player's turn: ")
    player_turn = input('''1 for scratch
2 for fireball 
3 for heal: ''')
    if player_turn == '1':
        print(f'player used scratch!! {player.scratch()} damage')
        comp_health -= player.scratch()
    elif player_turn == '2':
        print(f'player used fireball!! {player.fireball()} damage')
        comp_health -= player.fireball()
    elif player_turn == '3':
        if player_health < 100:
            print(f'player used heal!! {player.heal()} gained')
            player_health += player.heal()
        else:
            print('already max health!')
    elif player_turn == 'exit':
        break
    else:
        print('invalid')
    print(f'remaining health of enemy {comp_health}')
    time.sleep(3)
    if comp_health <= 0:
        print('enemy is down. YOU WON')
        break

    comp_turn = random.randint(1, 3)
    print()
    print("enemy's turn: ")
    time.sleep(3)
    if comp_turn == 1:
        print(f'enemy used scratch!!{comp.scratch()} damage')
        player_health -= comp.scratch()
    elif comp_turn == 2:
        print(f'enemy used thunderbolt!!{comp.thunderbolt()} damage')
        player_health -= comp.thunderbolt()
    elif comp_turn == 3:
        if comp_health < 100:
            print(f'enemy used heal!!{comp.heal()} gained')
            comp_health += comp.heal()
        else:
            print('already max health!')
    else:
        print('invalid')
    print(f'remaining health of player {player_health}')
    time.sleep(3)
    if player_health <= 0:
        print('you are down. YOU LOOSE')
        break
