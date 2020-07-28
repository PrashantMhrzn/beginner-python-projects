def decor(fun):
    def wrap(num):
        print('*****Welcome!!!*****')
        fun(num)
        print('*****Thankyou!!!*****')
    return wrap


@decor
def mul_table(num):
    ans = 0
    for i in range(1, 11):
        ans = num * i
        print(f'{num} * {i} = {ans}')
    return ''


usr_inp = int(input('enter a number to see their multiplication table: '))
print(mul_table(usr_inp))
