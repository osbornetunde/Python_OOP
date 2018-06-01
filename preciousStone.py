class preciousStone:
	
	preciousStoneCollection = []
	numberOfPreciousStone = 0


	def __init__(self, stone):
		self.stone = stone
		preciousStone.numberOfPreciousStone += 1
		

		if preciousStone.numberOfPreciousStone <= 5:
			preciousStone.preciousStoneCollection.append(self)
			
		else:
			del preciousStone.preciousStoneCollection[0]
			preciousStone.preciousStoneCollection.append(self)

	@staticmethod
	def displayPreciousStone():
		for PreciousStone in preciousStone.preciousStoneCollection:
			print(PreciousStone.stone, end = ' ')
		print()

preciousStoneOne = preciousStone("Gold")
preciousStoneTwo = preciousStone("Diamond")
preciousStoneThree = preciousStone("Sapphire")
preciousStoneFour = preciousStone("Emerald")
preciousStoneFive = preciousStone("onyx")

preciousStoneFive.displayPreciousStone()
preciousStoneSix = preciousStone("Amber")
preciousStoneSix.displayPreciousStone()
	




