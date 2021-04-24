# -"""
coins = [10, 50, 100, 500]
chagne = 400
total = 0
for i in range(len(coins)):
    coin = coins[i]
    if chagne // coin >= 1:
        total = total + chagne // coin
        chagne = chagne - coin * (chagne//coin)
        print(total, chagne)
"""
"""

fibo = []
for x in range(0, 10):
    if x < 2:
        fibo.append(1)
    else:
        fibo.append(fibo[x-2] + fibo[x-1])

print(fibo)
"""
""
input_id = input("enter the id : ")
input_pw = input("enter the pw : ")

def login_check(input_id, input_pw):
    f = open('text1','r')
    lines = f.readlines()
    flag = False
    for line in lines:
        temp = line.split('\n')[0]
        id, pw = temp.split(',')
        if id == input_id and pw == input_pw:
            flag = True
            break
    return flag
flag = login_check(input_id, input_pw)
if flag:
    print("succes")
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
        if map[0] == map[1] == map[2] != '#':
            check = True
        elif map[0] == map[3] == map[6] != '#':
            check = True
        elif map[3] == map[4] == map[5] != '#':
            check = True
        elif map[1] == map[4] == map[7] != '#':
            check = True
        elif map[6] == map[7] == map[8] != '#':
            check = True
        elif map[2] == map[5] == map[8] != '#':
            check = True
        elif map[0] == map[4] == map[8] != '#':
            check = True
        elif map[2] == map[4] == map[6] != '#':
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
                num = random.randrange(0, 8)
                if nk_map[num] == "#":
                    nk_map[num] = b
                    break
            turn = 0
        print("----------------------------- again")
        print_map(nk_map)
        nk_win_check = check_win(nk_map)

        if nk_win_check:
            break
else:
    print("fail")
