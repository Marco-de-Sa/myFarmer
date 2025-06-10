import PlantingMain, findingNemo

clear()
while True:
    # PlantingMain.cycle("bush")
    # use_item(Items.Weird_Substance)
    plant(Entities.Bush)
    n_substance = get_world_size() ** 2
    use_item(Items.Weird_Substance, n_substance)
    findingNemo.findTreasure()
