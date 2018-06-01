# Public as memberName
# Protected as _memberName
# Private as __memberName

class Car:
	numberOfWheels = 4
	_color = "Black"
	__yearOfManufacture = 2017

class Bmw(Car):
	# def __init__(self):
	# 	print("Protected attribute color: ", self._color)
	model = "s6"
	print("model for the year: ", model)

class Tesla(Bmw):
	def __init__(self):
		print("Protected attribute color: ",self._color)

car = Car()
print("Public attribute numberOfWheels: ", car.numberOfWheels)
tesla = Tesla()
print("Private attribute yearOfManufacture: ", car._Car__yearOfManufacture)