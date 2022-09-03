#Show how the program run
n = int(input())
name = [0]*n
time = [0]*n
for i in range (n):
    x = input().split()
    key = x[0]
    value = int(x[1])
    if key == 't':
        name[i] = key
        time[i] = 0
        counter = i-1
        check = False
        while counter >=0:
            if name[counter] != 't' and time[counter] != 0:
                if time[counter] > value:
                    print(name[counter])
                    time[counter] -= value
                    value = 0
                    check = True
                    break
                else:
                    value -= time[counter]
                    time[counter] = 0
            counter-=1
        if value != 0 or check is False:
            print('main')
    else:
        name[i] = key
        time[i] = value