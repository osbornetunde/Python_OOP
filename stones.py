class PreciousStone:
	numbersOfPreciousStone = 0
	preciousStoneCollection = []

	def __init__(self, name):
		self.name = name

		PreciousStone.numbersOfPreciousStone += 1
		if PreciousStone.numbersOfPreciousStone <= 5:
			PreciousStone.preciousStoneCollection.append(self)

		else:
			del PreciousStone.preciousStoneCollection[0]
			PreciousStone.preciousStoneCollection.append(self)

	@staticmethod
	def displayPreciousStone():
		for preciousStone in PreciousStone.preciousStoneCollection:
			print(preciousStone.name, end=" ")
		print()


preciousStoneOne = PreciousStone("Gold")
preciousStoneTwo = PreciousStone("Diamold")
preciousStoneThree = PreciousStone("sapphire")
preciousStoneFour = PreciousStone("Ruby")
preciousStoneFive = PreciousStone("Emerald")
preciousStoneFive.displayPreciousStone()
preciousStoneSix = PreciousStone("onyx")
preciousStoneSix.displayPreciousStone()