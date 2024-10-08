from steps_pkg.homepage import show_homepage
# show_homepage() # test
database = {"admin":"password123"}
quotes = []
authorized_user = ""

while True:
	show_homepage()

	if authorized_user == "":
		print("You have to be logged in first.")
	else:
		print("Logged in as: ", authorized_user)
