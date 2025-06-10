import goTo


def Till():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            harvest()
            till()
            if get_water() < 0.75:
                use_item(Items.Water)
            plant(Entities.Sunflower)
            move(North)
        move(East)
    harvestAll()


def CheckHarvest():
    coords = []
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_entity_type() == None:
                coords.append([get_pos_x(), get_pos_y()])
            move(North)
        move(East)
    while coords:
        for pos in coords[:]:  # iterate over a copy
            goTo.goTo(pos[0], pos[1])
            if get_entity_type() != Entities.Pumpkin:
                plant(Entities.Pumpkin)
                plant(Entities.Pumpkin)
                use_item(Items.Fertilizer)
            else:
                coords.remove(pos)
        if len(coords) == 0:
            harvest()
            goTo.goTo(0, 0)
            break


def harvestAll():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_water() < 0.75:
                use_item(Items.Water)
            harvest()
            move(North)
        move(East)


def plantTree():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            harvest()
            if get_water() < 0.75:
                use_item(Items.Water)
            if i % 2 == 1:
                if j % 2 == 1:
                    if get_ground_type() == Grounds.Grassland:
                        till()
                    plant(Entities.Tree)
                else:
                    if get_ground_type() == Grounds.Grassland:
                        till()
                    plant(Entities.Bush)
            if i % 2 == 0:
                if j % 2 == 0:
                    if get_ground_type() == Grounds.Grassland:
                        till()
                    plant(Entities.Tree)
                else:
                    if get_ground_type() == Grounds.Grassland:
                        till()
                    plant(Entities.Bush)
            move(North)
        move(East)


def PlantPumpkin():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_water() < 0.75:
                use_item(Items.Water)
            harvest()
            plant(Entities.Pumpkin)
            use_item(Items.Fertilizer)
            move(North)
        move(East)
    CheckHarvest()
    return


def cycle(PlantType):
    for i in range(get_world_size()):
        i = 0
        while True:
            if get_water() < 0.75:
                use_item(Items.Water)
            if can_harvest() or get_entity_type() == None:
                harvest()
                if PlantType == "bush":
                    if get_ground_type() == Grounds.Grassland:
                        till()
                    plant(Entities.Bush)
                elif PlantType == "carrot":
                    if get_ground_type() == Grounds.Grassland:
                        till()
                    plant(Entities.Carrot)
                elif PlantType == "grass":
                    if get_ground_type() == Grounds.Grassland:
                        till()
                    plant(Entities.Grass)
                elif PlantType == "sunflower":
                    if get_ground_type() == Grounds.Grassland:
                        till()
                    plant(Entities.Sunflower)
                elif PlantType == "tree":
                    plantTree()
                    return
                elif PlantType == "pumpkin":
                    PlantPumpkin()
                elif PlantType == "cactus":
                    if get_ground_type() == Grounds.Grassland:
                        till()
                    plant(Entities.Cactus)
                move(North)
                i += 1
                if i == get_world_size():
                    break
        move(East)


def walkTheDinosaur():
    counted = 0
    if get_world_size() % 2 == 1:
        while True:
            if get_pos_x() == get_world_size() - 1 and get_pos_y() > get_world_size() // 2:
                goTo.goTo(0, 0)
                counted += 1
            elif get_pos_x() == get_world_size() - 1 and get_pos_y() < get_world_size() // 2:
                goTo.goTo(get_world_size() - 1, get_world_size() - 1)
                goTo.goTo(0, get_world_size() - 1)
                goTo.goTo(0, 0)
                goTo.goTo(get_pos_x() + 1, get_pos_y())
                goTo.goTo(get_pos_x(), get_pos_y() + 1)
                counted += 1
            elif get_pos_y() == 0:
                goTo.goTo(get_pos_x() + 1, get_world_size() - 2)
            elif get_pos_y() == get_world_size() - 1:
                goTo.goTo(0, 0)
            elif get_pos_y() == get_world_size() - 2:
                goTo.goTo(get_pos_x() + 1, 1)
            elif get_pos_y() == 1:
                goTo.goTo(get_pos_x() + 1, get_world_size() - 2)

            if counted == get_world_size() * 2 // 1:
                return
    else:
        while True:
            if get_pos_x() == get_world_size() - 1:
                goTo.goTo(0, 0)
                counted += 1
            elif get_pos_y() == 0:
                goTo.goTo(get_pos_x() + 1, get_world_size() - 1)
            elif get_pos_y() == get_world_size() - 1:
                goTo.goTo(0, 0)
            elif get_pos_y() == get_world_size() - 1:
                goTo.goTo(get_pos_x() + 1, 1)
            elif get_pos_y() == 1:
                goTo.goTo(get_pos_x() + 1, get_world_size() - 1)

            if counted == get_world_size() * 2 // 1:
                return