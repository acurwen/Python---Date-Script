# Welcome message
print("Hello and welcome to Python Palace!")
user = input("Please enter your name: ")
dateName = input("Please enter your date's name: ")
print("Welcome", user , "and", dateName + "!")

# Asking for budget
print(user + ", please enter your date budget: ")
budget = input("Date budget: ") #have to make sure this is a integer or float; maybe type cast it
print("You've inputted", budget, "as your date budget.")

# Presenting menu
print("Here's our menu at Palace:")

# Taking order -- has to be a loop
userorder1 = input("What would you like to order (food)?: ")
dateorder1 = input("What would your date like to order (food): ")

# Calculating Orders: Here add up prices of both userorder1 and date order1 and subtract from budget
remaining = 1 + 1
print("Okay, that sums up to $", remaining,"of your budget remaining.")
orderMore = input("Would you like to order some more? (y/n): ")
#if orderMore == y

# User and date eating food ordered 
print("Great! Enjoy your food.")
# time.sleep(5) # have to import 'time'

# Asking user to pay and share meal. 
print("Hello! I hope you both enjoyed your meal.")
print(user , ", can you come with me over here?")
print("...walking")
payAnswer = input("Will you be paying for this meal? (y/n): ")

# If they don't pay
# if payAnswer == n, then
print("That's alright.", dateName, "has you both covered.")
print("Unfortunately, however, this will be the last date the two of you share.")
print("*Mr. Krabs violin*")

# If they do pay
# if payAnswer == y
# then 
print("Great! Your final bill is: $")

# If under budget
print("Oh dear, it looks like you are out of funds. Guess you will have to head to the kitchen and wash dishes.")
print("And look at that...your date has left!")

# If over budget
print("Looks like you have enough to pay.")
print("Thanks for eating here at Python Palace. Looks like", dateName, "is interested in a second date!")

# If over budgger, but dateOrder is any of the appetizers, user will not get a date.
print("Looks like you have enough to pay.")
print("Thanks for eating here at Python Palace. By the way", dateName, "happens to not believe in appetizers and was pretty disappointed you ordered them! They just don't think you two are right for each other. Have a goodnight!")
