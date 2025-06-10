def goTo(x, y):
    nx, ny = get_pos_x(), get_pos_y()
    if ny > y:
        while True:
            move(South)
            ny = get_pos_y()
            if y == ny:
                break
    elif ny < y:
        while True:
            move(North)
            ny = get_pos_y()
            if y == ny:
                break

    if nx > x:
        while True:
            move(West)
            nx = get_pos_x()
            if x == nx:
                break
    elif nx < x:
        while True:
            move(East)
            nx = get_pos_x()
            if x == nx:
                break


def goToX(x, y):
    nx, ny = get_pos_x(), get_pos_y()
    if nx > x:
        while True:
            move(West)
            nx = get_pos_x()
            if x == nx:
                break
    elif nx < x:
        while True:
            move(East)
            nx = get_pos_x()
            if x == nx:
                break
    if ny > y:
        while True:
            move(South)
            ny = get_pos_y()
            if y == ny:
                break
    elif ny < y:
        while True:
            move(North)
            ny = get_pos_y()
            if y == ny:
                break
