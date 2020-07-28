def armstong(num):
    if len(num) > 1:
        count = len(num)
        arm = 0
        for i in num:
            arm += (int(i)**count)
        return f'{num} is an Armstrong' if arm == int(num) else f'{num} is not an Armstrong'
    else:
        return 'All one digit numbers are Armstrong numbers!'


try:
    usr_inp = input('Enter a number to check if Armstrong: ')
    print(armstong(usr_inp))
except ValueError:
    print('Enter a number!!')
