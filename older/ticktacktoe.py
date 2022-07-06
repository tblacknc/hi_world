
graph = []
lines = ['0,1,2', '3,4,5', '6,7,8', '0,4,8', '2,4,6', '0,3,6', '1,4,7', '2,5,8']


def drawBox():
    print('\n' * 10)
    print(" ", graph[0], " | ", graph[1], " | ", graph[2])
    print("----------------")
    print(" ", graph[3], " | ", graph[4], " | ", graph[5])
    print("----------------")
    print(" ", graph[6], " | ", graph[7], " | ", graph[8])


def mePick():
    #broken
    cnt = 1
    while cnt:
        print('Enter your box:')
        y = input()
        y = int(y)
        y -= 1
        if graph[y] == ' ':
            graph[y] = 'X'
            cnt = 0
        else:
            print("that space is taken, try again")


def checkTwo(inp):
    # line = 0
    for x in lines:
        cells = x.split(',')
        line = 0
        for cell in cells:
            cell = int(cell)
            if graph[cell] == inp:
                line = line + 1
                if line == 2:
                    for cell2 in cells:
                        cell2 = int(cell2)
                        if graph[cell2] == ' ':
                            graph[cell2] = 'O'
                            return 1
    return 0


def checkWin():
    line = [0, 0]
    count = 0
    temp = 0
    for x in lines:
        cells = x.split(',')
        line[0] = 0
        line[1] = 0
        for cell in cells:
            cell = int(cell)
            entries = ['X', 'O']
            for entry in entries:
                if count == 1:
                    count = 0
                else:
                    count += 1
                if graph[cell] == entry:
                    temp = temp + 1
                    line[count] += 1
                    if line[count] == 3:
                        print("Game Over ", entry, ' wins!')
                        return 1
    return


def youPick():
    corners = [0, 2, 6, 8]
    sides = [1, 3, 5, 7]
    two = checkTwo("O")
    if two:
        return 1
    two = checkTwo("X")
    if two:
        return 1
    for corner in corners:
        corner = int(corner)
        if graph[corner] == " ":
            graph[corner] = "O"
            return 1
    if graph[4] == " ":
        graph[4] = "O"
        return 1
    for side in sides:
        side = int(side)
        if graph[side] == " ":
            graph[side] = "O"
            return 1


x = 0
while x < 9:
    graph.append(' ')
    x += 1

a = 1
drawBox()
count = 0
while a:
    if count == 5:
        print("Game Over TIE!")
        break
    mePick()
    drawBox()
    if checkWin():
        break
    youPick()
    drawBox()
    if checkWin():
        break
    count += 1

