def armstong(num):
    if len(num) > 1:
        count = len(num)
        arm = 0
        for i in num:
            arm += (int(i)**count)
        if arm == int(num):
            print(f'{num} is an Armstrong') 
        else:
            print(f'{num} is not an Armstrong') 
    else:
        print('All one digit numbers are Armstrong numbers!')


try:
    usr_inp = input('Enter a number to check if Armstrong: ')
    armstong(usr_inp)
except ValueError:
    print('Enter a number!!')
