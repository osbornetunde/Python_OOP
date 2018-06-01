class Rental:
	def __init__(self, availableCars):
		self.car = availableCars
	def searchForCar(self, carType, days):
		if carType == "Hatchback":
			info = 30 * days
			print("Cost of Hatchback:$ ", info)
			print()
		elif carType == "Sedan":
			info = 50 * days
			print("Cost of Sedan:$ ", info)
			print()
		elif carType == "SUV":
			info = 100 * days
			print("Cost of SUV:$ ", info)
			print()
		else:
			print("That car is not available,Thank you!")


class Customer:
	def typeOfCar(self):
		print()
		print("Enter the type of car you want to rent: ")
		self.requestedCar = input()
		return self.requestedCar

	def numberOfDays(self):
		print()
		print("Enter number of days for use: ")
		self.daysOfUse = input()
		return self.daysOfUse



rental = Rental(['Hatchback', 'Sedan', 'SUV'])
customer = Customer()


carType = customer.typeOfCar()
days =  int(customer.numberOfDays())
rental.searchForCar(carType, days)
