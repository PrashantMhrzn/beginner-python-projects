bottles = 99
while bottles > 0:
    if bottles > 1:
        print(f'{bottles} bottles of beer on the wall')
        print(f'{bottles} bottles of beer, take one down pass it around. \n')
    else:
        print(f'{bottles} bottle of beer on the wall')
        print(f'{bottles} bottle of beer, take one down pass it around. \n')
        print(
            'No beer left for anyone to drink, my heart is heavy and is about to sink :(')
    bottles -= 1
