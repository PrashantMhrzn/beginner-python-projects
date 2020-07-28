def armstong():
    inp=input("enter a num: ")
    count=len(inp)
    arm=0
    for i in inp:
        arm+=(int(i)**count)
    if arm == int(inp):
        print("armstrong")
    else:
        print("not armstrong")

armstong()
