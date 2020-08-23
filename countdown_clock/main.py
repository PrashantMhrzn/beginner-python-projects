import time

def countdown(total_sec):
    while total_sec != 0: 
        time.sleep(1)
        if total_sec == 1:
            print('1 second')
        else:
            print(f'{total_sec} seconds')
        total_sec-=1


try:
    usr_inp = input('Start count down at: <sec> <space> <min> <space> <hour>(enter 0 to pass none)')
    smh=usr_inp.split()
    min_to_sec=int(smh[1])*60
    hour_to_sec=int(smh[2])*3600
    total_sec=hour_to_sec+min_to_sec+int(smh[0]) 
    countdown(total_sec)
except:
    print('Enter appropriate values!')
    
print('countdown over')
try:
    go=input('start over?(y/n)')
    if go == 'y':
        countdown(total_sec)
    elif go == 'n':
        print('exiting')
    else:
        print("Please enter 'y' or 'n'!!!")
except ValueError:
    print("Please enter 'y' or 'n'!!!")