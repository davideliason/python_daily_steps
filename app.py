from steps_pkg.homepage import show_homepage, give_quote, show_quotes
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
		if authorized_user =='':
			print("You are not logged in")
		else:
			quote_string = give_quote(authorized_user)
			quotes.append(quote_string)

	elif option == '4':
		# list quotes fx
		show_quotes(quotes)

	elif option == '5':
		# say goodbye and exit
		print("Goodbye")
		exit()

	elif option == '6':
		print("good choice")



