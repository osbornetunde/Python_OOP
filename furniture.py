class Furniture:
	typeOfWood = 'Teakwood'
	_numberOflegs = 4


class Chair(Furniture):
	def __init__(self):
		print("The typeOfWood used for this chair is {} and it has {} legs".format(self.typeOfWood, self._numberOflegs))
	def changeWoodType(self,typeOfWood):
		self.typeOfWood = typeOfWood
		print("The typeOfWood used for this chair is {} and it has {} legs".format(self.typeOfWood, self._numberOflegs))

chair = Chair()




while True:
	print("Enter 1 to display info")
	print("Enter 2 to change type of wood")
	print("Enter 3 to quit")

	userChoice = int(input())
	if userChoice is 1:
		chair = Chair()
	elif userChoice is 2:
		print("Enter the type of wood: ")
		typeOfWood = input()
		chair.changeWoodType(typeOfWood)
	elif userChoice is 3:
		quit()

