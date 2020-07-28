def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return f'{num} is not a prime number'
        else:
            return f'{num} is a prime number'
    else:
        return f'{num} is not a prime number'


usr_inp = int(input('Enter a number to check if prime: '))
print(is_prime(usr_inp))
