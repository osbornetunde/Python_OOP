class Furniture:
	typeOfWood = Teakwood
	__numberOflegs = 4


class Chair(Furniture):
	def __init__(self):
		print("The typeOfWood used for this chair is {} and it has {} legs".format(self.typeOfWood, self.__numberOflegs))

chair = Chair()
