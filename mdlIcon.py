def smallTick(x, y):
    cords = []
    cords.append((x, y+2))
    cords.append((x+1, y+3))
    cords.append((x+2, y+2))
    cords.append((x+3, y+1))
    cords.append((x+4, y))

    return cords

def smallCross(x,y):
    cords = []

    cords.append((x, y + 3))
    cords.append((x, y + 0))
    cords.append((x + 1, y + 2))
    cords.append((x + 1, y + 1))
    cords.append((x + 2, y + 2))
    cords.append((x + 2, y + 1))
    cords.append((x + 3, y + 3))
    cords.append((x + 3, y + 0))

    return cords

def smallCont(x,y):
    cords = []

    cords.append((x, y + 3))
    cords.append((x, y + 2))
    cords.append((x, y + 1))
    cords.append((x+1, y + 2))
    cords.append((x+1, y))
    cords.append((x+2, y+1))
    cords.append((x+3, y+1))
    cords.append((x+4, y+2))
    cords.append((x+4, y))
    cords.append((x+5, y+3))
    cords.append((x+5, y+2))
    cords.append((x+5, y+1))

    return cords


def TB(x,y,num):
    cords = []
    cords.append((x, y))
    cords.append((x+1, y))
    cords.append((x+2, y))
    cords.append((x+1, y+1))
    cords.append((x+1, y+2))
    cords.append((x+1, y+3))
    cords.append((x+4, y))
    cords.append((x+4, y+1))
    cords.append((x+4, y+2))
    cords.append((x+4, y+3))
    cords.append((x+5, y+1))
    cords.append((x+5, y+3))
    cords.append((x+6, y+2))

    if num == 1:
        cords.append((x+8, y))
        cords.append((x+9, y))
        cords.append((x+8, y+3))
        cords.append((x+9, y+1))
        cords.append((x+9, y+2))
        cords.append((x+9, y+3))
        cords.append((x+10, y+3))
    elif num == 2:
        cords.append((x + 8, y))
        cords.append((x + 8, y+2))
        cords.append((x + 8, y+3))
        cords.append((x + 9, y+1))
        cords.append((x + 9, y+3))
        cords.append((x + 10, y+3))

    return  cords