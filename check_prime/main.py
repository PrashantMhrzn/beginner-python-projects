def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                print("not prime")
                break
        else:
            print("prime")
    else:
        print("not prime")


usr_inp = int(input('enter a number to check if prime: '))
is_prime(usr_inp)
