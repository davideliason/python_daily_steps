from steps_pkg.homepage import show_homepage, give_quote, show_quotes
from steps_pkg.user import login, register
import json

# show_homepage() # test
database = {"admin":"123"}
quotes = []
authorized_user = ""
steps = [{"user": "Alice", "date": "2024-10-10", "steps" :{"weight": 160, "pushups": 20}}]

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
	    steps.append({"name": authorized_user})

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
		if authorized_user =='':
			print("You are not logged in")
		else:
			
			date = input("What is the date (MM-DD-YY)? ")
			weight = input("What is your weight?")
			steps.append({"user": authorized_user, "date": date, "weight":weight})

			# Save to JSON
			with open("steps.json", "w") as f:
				json.dump(steps, f)

			# Retrieve from JSON
			with open("steps.json", "r") as f:
				loaded_data = json.load(f)

			# Access a specific date
			# print(loaded_data) # print whole data object for testing purposes
			for person in loaded_data:
				for key in person:
					print(f"{key} = {person[key]}")

	elif option == '7':
		if authorized_user =='':
			print("You are not logged in")
		else:
			search_query = input("What date to look for? ")
			print(f"ok looking for {search_query}")

			# Retrieve from JSON
			with open("steps.json", "r") as f:
				loaded_data = json.load(f)

			for data in loaded_data:
				for key in data:
					if key == 'user' and data[key] == username:
						print(f'Weight: {data["weight"]}')
						next
						
					else:
						continue
						exit
