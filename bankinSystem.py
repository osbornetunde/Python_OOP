import random

class Account:

	accountDetails = {'Tunde':[300,89047],'Kolade':[500,43958],'Lara':[1000,39865]}
	def __init__ (self):
		pass
		
		
		

	def createAccount(self, name, initialDeposit, accountNumber):
		Account.accountDetails[name] = initialDeposit, accountNumber
		return Account.accountDetails[name]
		
	def generateAccountNumber(self):
		ran = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], k=5)
		str1 = ''.join(str(e) for e in ran)
		return str1


	def withdraw(self):
		print("Enter amount to withdraw: ")
		amountWithdrawn = int(input())
		if amountWithdrawn > Account.accountDetails[name][0]:
			print("Insufficient balance")
		else:
			Account.accountDetails[name][0] = Account.accountDetails[name][0] - amountWithdrawn
			print("Your new account balance is:${}".format(Account.accountDetails[name][0]))
		print()


	def deposit(self):
		print("Enter amount to deposit: ")
		amountDeposited = int(input())
		Account.accountDetails[name][0]= Account.accountDetails[name][0] + amountDeposited
		print("Your new account balance is:${}".format(Account.accountDetails[name][0]))


	def displayAccountDetails(self, name, accountNumber):
		#print(name)
		if name in Account.accountDetails.keys():
			if Account.accountDetails[name][1] == accountNumber:
				print("Authentication Successful!")
				balance, acctNumber = Account.accountDetails.get(name)
				print("Your account balance is:${}".format(balance))
				print("Would you like to withdraw or deposit into your account? Y/N ")
				userChoice = input()
				if userChoice is 'Y':
					print("To withdraw press 'W', to deposit press 'D'")
					answer = input()
					if answer is 'W':
						self.withdraw()
					if answer is 'D':
						self.deposit()
				else:
					print("Thank you, for banking with us!")
					quit()
			else:
			 	print("Authentication failed")
		else:
			print("Sorry, you dont have an account with us. Thank you")
		

class Customer(Account):
	def newUser(self):
		print("Enter your name: ")
		self.name = input()
		print("Enter initial deposit: ")
		self.initialDeposit = int(input())
		print("Generating account number for {} .....".format(self.name))
		self.accountNumber = self.generateAccountNumber()
		print("Your account number is: {}".format(self.accountNumber))
		return  self.name, self.initialDeposit, self.accountNumber

	def existingUser(self):
		print("Enter your name: ")
		self.name = input()
		print("Enter account number: ")
		self.accountNumber = int(input())
		return self.name, self.accountNumber


account = Account()
customer = Customer()

while True:
	print("Are you an existing user? Y/N")
	user = input()
	if user is 'Y':
		name, accountNumber= customer.existingUser()
		#print(name, accountNumber)
		account.displayAccountDetails(name, accountNumber)
	elif user is 'N':
		print("Do you want to open an account? Y/N")
		choice = input()
		if choice is 'Y':
			name, initialDeposit, accountNumber = customer.newUser()
			#print(name, initialDeposit, accountNumber )
			account.createAccount(name, initialDeposit, accountNumber)
			account.displayAccountDetails(name, accountNumber)
		elif choice is 'N':
			print("Goodbye!")
			quit()
