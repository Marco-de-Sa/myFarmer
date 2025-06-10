import PlantingMain
#clear()
#PlantingMain.Till()
while True:
	clear()
	PlantingMain.cycle("sunflower")
	PlantingMain.harvestAll()
	clear()
	change_hat(Hats.Dinosaur_Hat)
	PlantingMain.walkTheDinosaur()
	unlock(Unlocks.Expand)