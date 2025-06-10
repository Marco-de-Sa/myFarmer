import PlantingMain
for j in range(10):
	clear()
	PlantingMain.Till()
	for i in range(2):
		PlantingMain.cycle("grass")
		PlantingMain.cycle("tree")
		PlantingMain.cycle("carrot")
		PlantingMain.cycle("cactus")
		if i % 2 == 0:
			PlantingMain.cycle("sunflower")
	PlantingMain.PlantPumpkin()