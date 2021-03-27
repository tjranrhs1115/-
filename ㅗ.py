def make_map():
    game_map = []
    for i in range(9):
        game_map.append("#")
    return game_map

def print_map(_map):

    print(nk_map[0] + '|' + nk_map[1] + '|' + nk_map[2])
    print('-----')
    print(nk_map[3] + '|' + nk_map[4] + '|' + nk_map[5])
    print('-----')
    print(nk_map[6] + '|' + nk_map[7] + '|' + nk_map[8])
nk_map = make_map()

def check_win(map):
    check = False
    if map[0] == map[1] == map[2]:
        check = True
    elif map[0] == map[1] == map[2]:
        check = True
    return check

a = 'o'
b = 'x'
turn = 0
import random
for i in range(9):

    if turn == 0:
        while True:
            num = int(input("Enter the your pusition : "))
            if nk_map[num] == "#":
                nk_map[num] = a
                break
        turn = 1
    else:
        while True:
            num = random.randrange(0,0)
            if nk_map[num] == "#":
                nk_map[num] = b
                break
        turn = 0
    print("----------------------------- again")
    print_map(nk_map)
    nk_win_check = check_win(nk_map)

    if nk_win_check:
        break