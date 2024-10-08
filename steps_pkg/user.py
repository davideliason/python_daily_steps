def login(database,username,password):
	if username in database and database[username] == password:
		print("Welcome!")
		return username
	elif username in database and database[username] != password:
		print("Invalid password!")
		return ''
	else:
		print("User not found!")
		return ''