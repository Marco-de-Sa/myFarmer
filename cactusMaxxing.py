import PlantingMain
clear()
counted = 0
while True:
	counted += 1
	PlantingMain.cycle("cactus")
	if counted%3 == 1:
		PlantingMain.cycle("sunflower")