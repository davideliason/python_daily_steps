# define function that will print the menu of actions for the user
def show_homepage():
	print('1. Login 2. Register 3. Enter Quote 4. Show Quotes 5. Logout')

def give_quote(username):
	new_quote = input("Enter new quote: ")
	quote_string = f"{username} gave this quote: {new_quote}"
	print("Thank you for giving this quote")
	return quote_string

def show_quotes(quotes):
	print("--All Quotes--")
	if not quotes:
		print("No quotes yet")
	else:
		for quote in quotes:
			print(quote)
