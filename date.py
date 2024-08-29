# DATE AT PYTHON PALACE

print("Hello and welcome to Python Palace!")

# User inputs who their date is
userName = input("What's your name? ")
dateName = input("Hey "+userName+ ", what's the name of your lucky date? ")
print(f"Well",userName+" and "+dateName+", we're excited you decided to dine here at Python Palace!")
print(" ")

# User inputs date budget
dateBudget = input("Hey "+userName+", what's your total budget for this date? In US dollars: $")
print("Your total date budget is $"+dateBudget+". Great!")
print(" ")

# Create restaurant menu
menu = {"lobster": 65.00,
        "steak": 55.00,
        "chowder": 25.00,
        "scampi": 30.00,
        "cobbler": 17.00,
        "martini": 15.50}

# Print restaurant menu
print(userName+" and "+dateName+", please take a look at our menu:")
print(" ")
print(" ~ Python Palace Menu ~ ")
for x, y in menu.items():
        print(x, y)
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# Empty list to keep track of orders
mealTab = []

# Empty tab to start        
totalBill = 0  
# dateBudget = 80

# while budget is over 0 
while True:
        order = input("What menu item would you like to order? Type 'x' when you are done with ordering: ") 
        
        # If order is in menu
        if menu.get(order):
                # add order to tab
                mealTab.append(order)
                print(f"Order: ",mealTab)
                print(f"Price of "+order+": ",menu.get(order))
                     
        # If ordering is over
        elif order == "x":
                break     

        # elif dateBudget <= 0:
        #         print("Insufficent funds. Cannot add more items to tab.")
        #         break

        # If order is not in menu       
        else:   
                print("Item not on menu.")
                

# new empty list for order prices
prices = []

# add each order's price to prices list
for order in mealTab:
        if order in menu:
                prices.append(menu[order])

# add price of all ordered items
sumOftab = sum(prices)

print(f"Your total is $",sumOftab)
remainingBudget = float(dateBudget) - sumOftab



while True:
# Asking user if they are paying 
        payAnswer = input("Will you be paying for this meal? (y/n): ")

# agree to pay
        if payAnswer == "y":
                print(f"Your remaining budget is $",remainingBudget)

        # if they spend all but 10 if their dollars, second date 
                if remainingBudget < 0:
                        print("Oh dear, it looks like you are out of funds to pay anyway. Guess you will have to head to the kitchen and wash dishes.")
                        print("And look at that..."+dateName+" has left!")
                        break
                
                elif remainingBudget <= 10:
                        print("It looks like you have enough funds to pay.")
                        print("Thanks for eating here at Python Palace. "+dateName+" is flattered you'd almost go broke for them! Looks like they're interested in a second date!")
                        break
                # if they have more than 10 dollars to their name after the date, no second date
                elif remainingBudget >= 10:
                        print("It looks like you have enough funds to pay.")
                        print("Thanks for eating here at Python Palace. Unfortunately, "+dateName+" thinks you didn't spend enough. No second date!")
                        break
  
        # don't agree to pay
        elif payAnswer == "n":
                print(f"That's alright. ",dateName, "has you both covered.")
                print("Unfortunately, however, this will be the last date the two of you share.")
                print("*Mr. Krabs violin*")
                break

        else: 
                print("Input not valid. Please enter y or n.")
