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


print(mul_table(5))
