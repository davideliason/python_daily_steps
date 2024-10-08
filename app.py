from steps_pkg.homepage import show_homepage
from steps_pkg.user import login, register

# show_homepage() # test
database = {"admin":"123"}
quotes = []
authorized_user = ""

while True:
	show_homepage()

	if authorized_user == "":
		print("You have to be logged in first.")
	else:
		print("Logged in as: ", authorized_user)

	option = input("Enter an option:")

	if option == '1':
	    # login functionality
	    username = input('Enter username: ')
	    password = input('Enter password: ')

	    authorized_user = login(database,username,password)


	elif option == '2':
		# register functionality
		username = input("Enter username: ")
		password = input("Enter password: ")

		authorized_user = register(database,username)

		# if database[username] is not in there, then return empty string
		if authorized_user != "":
			database[username] = password
			authorized_user = username

	elif option == '3':
		# make quote functionality
		print("make quote fx")
		show_homepage()

	elif option == '4':
		# list quotes fx
		print("make list quotes fx")
		show_homepage()

	elif option == '5':
		# say goodbye and exit
		print("Goodbye")
		exit()



