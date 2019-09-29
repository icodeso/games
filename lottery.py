import random
print('---------- LOTTERY GAME ----------')
play = 'yes'

pick = []
draw = []

while play == 'yes':
    print('Choose your numbers (1-49)')
    for i in range(6):
        while len(pick) < 6:
            p = int(input(f'{i + 1}. '))
            if p not in pick:
                    if p in range(1,50):
                        pick.append(p)
                        print(pick)
                        draw.append(random.randint(1,50))
                        i+=1
                    else:
                        print('Your number is out of range. Choose again.')
            else:
                print('Your number is already on the list. Choose1 again.')
    match = 0
    for num in pick:
        if num in draw:
            match += 1
    print(f'\nLast draw:\n{sorted(draw)}')
    print(f'\nYour result: {match} matching numbers\n')
    pick.clear()
    draw.clear()
    play = input('Would you like to play again? (yes/no)')
    while play != 'yes':
        if play == 'no':
            exit()
        elif play != 'yes':
            play = input('Would you like to play again? (yes/no)')

