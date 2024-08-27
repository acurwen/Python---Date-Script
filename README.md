# Python Date Script

## Purpose:
I create a date simulator that asks the user who their date is, their budget for the date and their restaurant order. Then the simulator calculates how much money the food ordered costs
and asks the user if they want to pay the bill. Based on the choices of the user, the date simulator will determine whether or not the user will get a second date. 

User inputs who is on the date with them
User inputs their budget for the date
Print the restaurant menu (your group created this!) 
User inputs their food/drink item choices from a restaurant menu list (for themselves and their date)
Script tells the user how much money they have left after each order.
At the end of the date user must agree to pay the bill and then their final budget is shown to them.
Challenge: Based on all the user inputs, the script should decide whether the user will get a second date or not and tell the user the decision.

## Initial Structure of Script:

I used the input() function to read input from the user with a prompt, ie.  `dateName = input("Please enter your date's name: ")`

I used the print() function to print out messages for each section and split my code into these sections using psuedo code.  

Writing my initial input and print statements in order of the instructions helped me to map out my script in an organized way to then figure out how to fill in those sections later. 
As I wrote my psuedo code each section, I realized that for the part where I ask the user for their order(s) and show how much money they have left over should be a while loop to 
allow the user to order multiple times and to have a standing function that keeps track of the budget everytime it's changed.

I updated the menu we made in groups to have a price for each item. 

After the user has finished all orders, I included a print command to say "Enjoy eating!" and a sleep command to simulate the date. The sleep equivalent in Python I found was time.sleep(), but I had to install the time command. 

For the challenge, if the user chooses to *both* pay for the meal and doesn't pick one of the meals the date dislikes, they will get a second date. I decided that the date would automatically strongly dislike 
ordering an appetizer because they believe in getting to the entree fast.

If the user doesn't offer to pay for the date, they will not get a second date. Also if they offer to pay, but have insufficient funds, the date will leave and will not be open to a second date. 
