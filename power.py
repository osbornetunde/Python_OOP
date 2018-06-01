class Square:
	def __init__(self, side):
		self.side = side

	def __pow__(squareOne, squareTwo):
		return(squareOne.side**squareTwo.side)



squareOne = Square(2)
squareTwo = Square(4)
print("The result of squareOne raised to squareTwo: ", squareOne**squareTwo)