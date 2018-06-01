class Rent:
	carDetails = {'Hatchback':30,'Sedan':50, 'SUV':100}
	def __init__(self):
		print("The cost of Hatchback:$ ",Rent.carDetails['Hatchback'])
		print("The cost of Sedan:$ ",Rent.carDetails['Sedan'])
		print("The cost of SUV:$ ",Rent.carDetails['SUV'])

	def displayFareDetails(self, daysOfUse, carType):
		self.fare = Rent.carDetails[carType] * daysOfUse
		print("Your fare for {} days is:${}".format(daysOfUse, self.fare))



class Customer:
	def numbeOfDays(self):
		print("Enter the number of days: ")
		self.daysOfUse = int(input())
		return self.daysOfUse

	def typeOfCar(self): 
		print("Enter the type of car you want to borrow: ")
		self.carType = input()
		return self.carType

rent = Rent()
customer = Customer()

while True:
	print("Enter 1 for available car")
	print("Enter 2 for request for a car")
	print("Enter 3 to quit")
	userChoice = int(input())
	if userChoice == 1:
		rent.displayFareDetails()
	if userChoice == 2:
		carType = customer.typeOfCar()
		daysOfUse = customer.numbeOfDays()
		rent.displayFareDetails(daysOfUse, carType)
	if userChoice == 3:
		quit()