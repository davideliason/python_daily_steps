# python_daily_steps
## Octcober 8, 2024
### David Eliason
an app to assist a user in capturing metrics in working towards their goals

#### Logic
There is the main file, app.py, and the steps_pkg module, which holds the functions that I call within app.py.

App.py runs a While True loop, and within that, prints out the menu of options, and examines the choice of a user. Depending on the choice selected, imported functions from the package are called using arguments populated by input methods.

Global variables of database (key-value dictionary), quotes, and authorized_user are used by the app.py file to not only keep track of whether a user is logged in or not, but to bridge the nested function calls. For example, if the user wants to give a quote, then the give_quote method will be called using the global quotes variable as an argument, appending the new quote.

This app explores the usage of a module, of importing functions, of passing variables as arguments, of using condional loops. There is plenty of room for adding additional features!
