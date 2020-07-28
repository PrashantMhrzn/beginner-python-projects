def is_prime(x):
    if x>1:
        for i in range(2,x):
            if (x%i)==0:
                print("not prime")
                break
        else:
            print("prime")
    else:
        print("not prime")

is_prime(2)  