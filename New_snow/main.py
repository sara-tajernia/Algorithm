class Point:
    def __init__(self, x, y, N, S, E, W):
        self.x = x
        self.y = y
        self.N = N
        self.S = S
        self.E = E
        self.W = W

def changeTime(pt, direction, time, list):
    if direction == 'N':
        x, y = 0, 1
        if pt.N != 1:
            pt.N = 1
            time += 5
        else:
            time += 1
    elif direction == 'S':
        x, y = 0, -1
        if pt.S != 1:
            pt.S = 1
            time += 5
        else:
            time += 1
    elif direction == 'E':
        x, y = 1, 0
        if pt.E != 1:
            pt.E = 1
            time += 5
        else:
            time += 1
    elif direction == 'W':
        x, y = -1, 0
        if pt.W != 1:
            pt.W = 1
            time += 5
        else:
            time += 1
    return time, changeInfo(pt, direction, list, x, y)


def changeInfo(pt, direction, list, x, y):
    check = False
    for i in range(len(list)):
        if list[i].x == pt.x + x and list[i].y == pt.y + y:
            if direction == 'N':
                list[i].S = 1
            elif direction == 'S':
                list[i].N = 1
            elif direction == 'E':
                list[i].W = 1
            elif direction == 'W':
                list[i].E = 1
            pt = list[i]
            check = True
            break
    if check == False:
        if direction == 'N':
            pot = Point(pt.x, pt.y + 1, 0, 1, 0, 0)
        elif direction == 'S':
            pot = Point(pt.x, pt.y - 1, 1, 0, 0, 0)
        elif direction == 'E':
            pot = Point(pt.x + 1, pt.y, 0, 0, 0, 1)
        elif direction == 'W':
            pot = Point(pt.x - 1, pt.y, 0, 0, 1, 0)
        pt = pot
        list.append(pot)
    return pt

if __name__ == '__main__':
    n = input()
    list = []

    for i in range (int(n)):
        list.clear()
        pt = Point(0, 0, 0, 0, 0, 0)
        list.append(pt)
        time = 0
        x = input()
        for j in range (len(x)):
            time, pt = changeTime(pt, x[j], time, list)

        print(time)