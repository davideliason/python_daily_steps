from steps_pkg.homepage import show_homepage
# show_homepage() # test
database = {"admin":"password123"}
quotes = []
authorized_user = ""


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

elif option == '2':
	# register functionality
	print("make register fx")
	show_homepage()

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



