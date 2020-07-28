def armstong(num):
    count = len(num)
    arm = 0
    for i in num:
        arm += (int(i)**count)
    if arm == int(num):
        print("armstrong")
    else:
        print("not armstrong")


try:
    usr_inp = input('enter a number to check if armstrong: ')
    armstong(usr_inp)
except ValueError:
    print('enter a number!!')
