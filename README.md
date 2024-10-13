# python_daily_steps
## Octcober 8, 2024
### David Eliason
an app to assist a user in capturing metrics in working towards their goals

#### Logic
There is the main file, app.py, and the steps_pkg module, which holds the functions that I call within app.py.

App.py runs a While True loop, and within that, prints out the menu of options, and examines the choice of a user. Depending on the choice selected, imported functions from the package are called using arguments populated by input methods.

Global variables of database (key-value dictionary), quotes, and authorized_user are used by the app.py file to not only keep track of whether a user is logged in or not, but to bridge the nested function calls. For example, if the user wants to give a quote, then the give_quote method will be called using the global quotes variable as an argument, appending the new quote.

This app explores the usage of a module, of importing functions, of passing variables as arguments, of using condional loops. There is plenty of room for adding additional features!

Description:
Daily Steps is an application written in Python that allows users to register, log in, and once authenticated, track metrics of various personal attributes or activities. These metrics are stored in a temporary version within the current version of the app, but the data is also concurrently stored in JSON format for future expansion to have the data persist in more durable fashion. The authenticated user has the ability to add inspirational quotes, and to search for specific dates for the metrics of interest corresponding to that date.

Initially, I penciled out pseudo-code and high-level process flow for the concept of the application and how the features might utilize the learning provided in the course. One of the course assignments featured user authentication and using lists for both storing and accessing data metrics, and I used that codebase as a starting point for the application code. As the course continued, I learned about dictionaries and how to access key-value values as well as flow control methodologies, and I was able to build added features to the application using nested dictionaries within a list. I also made modification using f-strings for displaying the values.

One aspect that I became more interested in exploring was the potential creation of a Class with build-in methods that could then be instantiated with an authorized user. That could be an extra dimension added to the code as a good exercise. One of the challenges that I came across was how to loop through a list of dictionary objects and then compare and/or obtain specific values. 

One example of this was looking for a specific weight value for a specific date value for a specific logged in and authenticated user: