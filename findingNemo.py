def findTreasure():
    directions = [North, East, South, West]
    index = 0

    def right(index):
        return (index + 1) % 4

    def left(index):
        return (index - 1) % 4

    lx, ly = get_pos_x(), get_pos_y()
    while True:
        index = left(index)
        if get_entity_type() == Entities.Treasure:
            harvest()
            return
        move(directions[index])
        if get_entity_type() == Entities.Treasure:
            harvest()
            return
        nx, ny = get_pos_x(), get_pos_y()
        if nx == lx and ny == ly:
            index = right(index)
            if get_entity_type() == Entities.Treasure:
                harvest()
                return
            move(directions[index])
            nx, ny = get_pos_x(), get_pos_y()
        if nx == lx and ny == ly:
            index = left(index)
            if get_entity_type() == Entities.Treasure:
                harvest()
                return
            move(directions[index])
            nx, ny = get_pos_x(), get_pos_y()
        if nx == lx and ny == ly:
            index = right(index)
            index = right(index)
            if get_entity_type() == Entities.Treasure:
                harvest()
                return
            move(directions[index])
            nx, ny = get_pos_x(), get_pos_y()

        lx, ly = get_pos_x(), get_pos_y()