input_id = input("enter the id : ")
input_pw = input("enter the pw : ")

def login_check(input_id, input_pw):
    f = open('가나와 친구들', 'r')
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
else:
    print("fail")



















































































































































