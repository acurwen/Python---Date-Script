# Python Date Script

## Purpose:
I created a date simulator where a user can choose their date budget, order food for themselves and their date, and see how much of their budget they have remaining after paying for their food. Based on the choices of the user, the date simulator will also determine whether or not the user will get a second date. 


## Initial Psuedo Code

While reading through the instuctions, I started off with writing pseudo code in my script. 

![image](https://github.com/user-attachments/assets/44e4e2bd-8035-4c8f-b737-015dc77e6a65)

Then based off the "task" of each section, I brainstormed what I'd likely need in each section code-wise.

For example, in the section where I ask the user for their order and show how much money they have left over, I thought I should write a while loop to allow the user to order multiple times. I'd also need a variable that keeps track of the dwindling budget every time the user made a new order.

Next, I filled in what I knew already, ie. how to read input using the input() function for who the user's date is and what their budget is: 
`dateName = input("What's the name of your lucky date? ")`

`dateBudget = input("What's your total budget for this date? In US dollars: $")`

## Restaurant Menu

To start off, I made a small dictionary menu that had a few food/drink items and corresponding prices. Although we created a menu in class, I needed to start off small to understand best how to print keys and values from it. Created a new psuedo section to actually create the restaurant menu. 

![image](https://github.com/user-attachments/assets/4ea360f6-5e55-4342-8882-e61490a50f0a)

Then I practiced printing the items of the menu with a for loop, using the .items() method to print out both the food and prices in a chart form. 

![image](https://github.com/user-attachments/assets/9e908683-bdc6-44b5-a250-bf4397a66b4a)

![image](https://github.com/user-attachments/assets/c5cd7fa4-c4ac-4941-80ad-c6db0c03d2b2)

Next, I needed to ask the user for their order. To do so, I created the variable "order" and set it equal to the input() function asking the user for their order. I figured to have the user be able to put in multiple orders, I put it in a while loop, so I wrote:
```
while True:
        order = input("What menu item would you like to order? ")` 
```

As I wanted, the question looped over and over again allowing the user to order multiple items. 

But I also wanted to include a way for the script to show if the user's order wasn't on the menu. So I wrote an if statement and used the 'not' keyword to say "if the order is not in the menu then, etc." So I wrote:
```
 if not menu.get(order):
                print("Item not on menu.")
```
Because I can't "get" the order (user's input) from my menu dictionary, it doesn't exist in the dictionary, so the user will be told the item's not on the menu. 

All together:

![image](https://github.com/user-attachments/assets/e712a044-3950-42b5-a7cc-faa3387cef4c)


As I ran the while loop, the code successfully presented the error message if a non-menu item was inputted and kept asking me what I wanted to order. 

![image](https://github.com/user-attachments/assets/c7d3715f-975b-4e9f-a63a-386290efda30)


So then I thought, I need a way to now keep track of everything ordered + the prices of each thing. And I realized, I didn't have a clause in my if statement that did any recording of the food ordered. I thought maybe I could make a list to keep track of everything ordered or another dictionary so that I could include the prices and maybe just copy over values from my menu dictionary into my new dictionary. The only issue with the second way is that I can't add duplicate keys to a dictionary so if the user wanted to order two steaks, the dictionary would only save one steak order. 

But I knew lists can have duplicates, so I created a list called mealTab that was empty. `mealTab = []` And I wrote in this empty list before my while loop.

Back in the if statement, I added an `else` clause (when the order does exist in the menu) and used the .append() method for lists. So if the order item exists in the menu, then append the order to the mealTab list. 

![image](https://github.com/user-attachments/assets/294d69e5-5b1d-4fb9-a559-6034019716fa)

I added in a print statement to print the mealTab list and testing worked! Everytime I entered an item that existed on the menu, the mealTab updated.

![image](https://github.com/user-attachments/assets/ac5f30ab-99e3-4fe1-abdb-f4d16218c090)

However, I wasn't getting the prices of the foods saved anywhere. 

I also realized I couldn't get to the prices if I didn't have a way to break out of the ordering while loop. So I made an elif statement, that if the user typed in 'x', the while loop would break. I added in the instructions about 'x' in the order prompt.

![image](https://github.com/user-attachments/assets/c3474e6b-7d38-4818-8edf-5f6f8d8bb986)

This, however, did not work in testing. When I typed in 'x', I'd get the error message I put in the first if clause. I figure that's because the first checkpoint I have in my if statement is checking for any input that doesn't match the menu -- which includes 'x'.

So I rewrote the first if without the 'not' to just say `if menu.get(order):` then `mealTab.append(order)`, kept the elif section the same and moved the error print message to the else section. Testing worked!


![image](https://github.com/user-attachments/assets/03fc61b7-94b6-46a6-bf98-a370829cd946)

![image](https://github.com/user-attachments/assets/730e1016-f22c-474b-8c7e-544b054de64c)

To keep track of the prices of each item ordered, I created a variable called totalBill and set it equal to 0. 

Then I decided to use a for loop to iterate over the items in the mealTab list since there are a set number of items (or arguments) in mealTab - after the while loop (ordering from the menu section).

So for each order in mealTab, I wanted to update totalBill with the price of each order. The price of each food item is the "value" in the menu dictionary and to return the values I needed the .get() method to return the value of the specified key. In this case, my specified key are all the orders in my mealTab list so I wrote:

```
for order in mealTab
  totalBill = totalBill + menu.get(order)
```

To test if this worked, I printed both the order and totalBill afterwards. 

![image](https://github.com/user-attachments/assets/e483a357-e062-423d-b5eb-63b6393c5168)

Testing worked and as expected the totalBill value incremented with each food item!

![image](https://github.com/user-attachments/assets/1e90c606-6966-4bb8-aecd-ce7c482acabc)

This project's instructions, however, state that the script should tell the user how much money they have left after each order. So I decided to nest this for loop in my previous if statement where I append the orders made to mealTab. I also created a variable earlier called dateBudget where the user inputs their budget and needed to keep track of that. 

First, I tried nesting the for loop to see if the output still worked. Had to move my totalBill variable up before the while loop next to where I created the empty mealTab list. Testing worked!

![image](https://github.com/user-attachments/assets/a54a8b0f-39a0-4b3e-b7d2-57325f2b25aa)

![image](https://github.com/user-attachments/assets/a44f4a09-752a-4953-9a30-d83295fab17c)

But, I still needed to instead showcase how much the user's budget they had left. Before, I had the dateBudget read as an input, but for testing purposes I saved it as $850 to start. Then I added in a third print statement to print the result of dateBudget - totalBill. Testing worked!

![image](https://github.com/user-attachments/assets/e5d3fd7d-8083-4176-a90a-0284af079956)


![image](https://github.com/user-attachments/assets/ae4bb9bb-c18c-4d0c-be81-0f732ce2e9ff)

I also added in some statements to the print commands to make the output clearer. 

![image](https://github.com/user-attachments/assets/051ef318-298d-4b6a-92e0-a073fd156188)


![image](https://github.com/user-attachments/assets/bfa42ae5-8c93-459e-9992-32abde844042)


As I kept adding orders, the dateBudget went into the negatives. Here I realized, I could add a condition in the while loop that makes it run until dateBudget <= 0, signifying that there's no more money to spend so no more orders can be added. 

So I rewrote the while loop to say `while dateBudget > 0:`

But then I had to include an if statement that if dateBudget <= 0, to break out of the while loop. I also wanted to print a message that said something like "Insufficent funds. Cannot add more items to tab." before the break. So I added in that if statement first (within the while loop), then changed my original if statement to add in orders to another elif statement. 

![image](https://github.com/user-attachments/assets/22cdd760-e941-4586-8724-8e2e4cdb3bf8)

This didn't work, however, as I tried maxing out the budget yet the while loop still ran when the budget was in the negatives. 
Then I changed the while loop to `while dateBudget >= totalBill:`. This faired better in testing as the while loop stopped running after the dateBudget hit the negatives, however, it only stopped running after the second hit in the negatives. 

![image](https://github.com/user-attachments/assets/de11d2e8-b61b-4951-9df3-d5e20a482c96)

I'm assuming this is because only after the first negative hit, does the script then check the value of dateBudget to see if it's less or equal to totalBill. No actually, I just realized that I declared dateBudget outside of the while loop and never add or subtract from it while in the while loop. So essentially, the while loop condition will always be true causing the script to never stop. 

So in my for loop that updates the tab, I added in a line that updated the value of dateBudget to be dateBudget minus the totalBill each time a menu item was added to the tab. This worked and the script stopped at the first negative value reported as the remaning budget. However, I noticed that in my output, the budget grew kind of fast, as in I didn't need too many food items to reach my budget of $850. I reviewed the prices of my menu and the food's expensive, but not that pricey to blow the budget so fast. 

I checked the math of the output and it was correct. Then I went back to the for loop and wrote out mental math of how my totalBill and dateBudget variables were updated to see if there was an issue there. 

![image](https://github.com/user-attachments/assets/aaf6a337-1334-4a33-bfe1-aadf72d93807)

Writing the math helped me immensely because I realized that each time I updated dateBudget, I subtracted the entire total bill from it instead of only the cost of the ordered item. So I changed it to `dateBudget = dateBudget - menu.get(order)`. My output made a lot more sense afterwards/took a longer time to reach the budget.

![image](https://github.com/user-attachments/assets/6ed6791b-0b85-453b-87a9-acc8b7833cfd)

I still had the issue however, of the script still allowing additions to the tab after the date budget was past zero. I also just noticed here that my output also included lines related to previous items added. Ideally, I'd only want the item's information to print when it's being added.

So I realized in my print statement that I'm printing "order" which would be every item in mealTab. Instead, I needed a way to print only the specific item so that the lines don't print for every current item in the mealTab list. I changed the 'order' in the for loop to 'i' and changed the print statement to print 'mealTab[i]' instead because I want the list to output only the information on the "i" menu item added each time. 
![image](https://github.com/user-attachments/assets/f710a1e6-5124-44a4-bb54-46edbc2c2c15)


But when running the script, I got an error that list indices must be integers or "slices" not strings. I realized I needed to add the range() and len() functions to go through the list. 

![image](https://github.com/user-attachments/assets/acf257e1-35d0-4ec9-a220-60470136c778)

Duplicate Output:


This did not fix my duplicate problem and gave me the same output as before. Here I also finally noticed that the duplicate lines were also messing with the calculations for dateBudget and totalBill because the previous menu items in the lists' prices were added and subtracted again. The math I wrote earlier helped me to confirm my totals weren't right when I added in one scampi and then one steak. 

![image](https://github.com/user-attachments/assets/9852a17c-94f5-4921-bf0a-f6fa3d80c88f)

I knew the issue lied somewhere in my print statements so I revisted those. Finally I realized, that I hadn't fixed my math before, because everytime the foor loop ran, totalBill and dateBudget were getting updated as many times as there were items in the mealTab list. 

mental math again:
![image](https://github.com/user-attachments/assets/588e7e22-3bc2-4d26-bbe6-f426fed11d27)

![image](https://github.com/user-attachments/assets/56f2c1b9-7559-422b-88d6-5ea1d5557725)

I realized here that the first output from ordering just steak was correct and matched my math (totalBill =  55.0; dateBudget =  795.0). However, when I added chowder to the mix, the next output of totalBill was totalBill plus the price of steak again AND plus the price of the chowder. It should only be the price of the chowder is here. So I Realized that I needed to take the addition and subtraction out of the four loops and instead add them up using my mealTab list outside of the for loop. 

So I took out the nested for loop entirely and had the if statement simply add in the orders to the mealTab list.

Then I tested if I could print the items in my mealTab list outside of the if statement - and I could using either `print(mealTab)` or
```
# print each order in list
for order in mealTab:
        print(order)
```

The latter one was better to get an itemized list of my mealTab items. 

Then I needed a way to use the items in mealTab as the "key" in my menu so that I could grab the prices of the items, or the "values."

So I made an for statement: for every order in mealTab, if it exists in the menu, then return the prices. I also needed another list to store the prices in, so I created another empty list called prices. So if the order in mealTab exists in menu, append it to the new prices list. Then I printed out prices to double check and I got the output I wanted. 

![image](https://github.com/user-attachments/assets/8866d03c-b53d-4280-b606-1f8bdb6ffd99)

![image](https://github.com/user-attachments/assets/43291359-8c9d-4eb5-bf35-81b303754670)

or
code:

![image](https://github.com/user-attachments/assets/40519493-1f10-4232-bac3-6c93180106d2)

output:

![image](https://github.com/user-attachments/assets/d6495d12-bb86-4e0f-9a51-48db4020d451)

Now I needed a way to add all the list prices together. I looked up how to add the values of a list together and found the sum() function. 
I created a new variable called sumOftab and set it equal to sum(prices). This worked to give me the total.

Moving on to the next step:

## Asking user to pay bill

Afterwards, I was able to easily display the order total and the user's remaining budget. I put these in print statements and then asked the user for input on if they want to pay for the meal. 

![image](https://github.com/user-attachments/assets/a83425b9-0307-49b8-afff-027b5219dda2)
![image](https://github.com/user-attachments/assets/027b3dbf-adf7-46af-bd91-925748b2af75)


Using an if statement, if they do pay, they get a checkout message. 
If they say no to paying, they will get a message that the covered the meal and there will be no second date message. Here, I also realized that I should have a check if the user surpassed their remaining budget. So I put that if remaining Budget is greater than zero, move on to the yes or no if statements and else (if the remaining budget is less than 0, print a message that the user has to come and clean the kitchen message. 

I changed my dateBudget to be $80 and tested ordering too much or little to test out my nested if statements and testing worked. 

![image](https://github.com/user-attachments/assets/9b2ca6eb-d3b5-41c6-b191-a615e26c3613)

![image](https://github.com/user-attachments/assets/3e25d6f2-0cba-4e97-8933-9491fbe98736)

-------------------------------------------------------
I also updated the outer while loop to say while budget >= 0; before it was just dateBudget > 0.
Ideally, I'd like the loop to stop allowing additions to the mealTab once there are insufficient funds or when an addition would . but for now I'll keep this version and move on to the rest of the script. 
## Starting with smaller menu

Created a small menu (based off the one we created in a group) to practice with that just had four key value pairs of foods and their corresponding prices.
Then I made an empty list called 'cart' to keep track of what the user orders and a variable named 'total' to keep track of the total price.

Used a for loop to print the keys and values like a menu and added in '$' and '.2f' to the values format output so that the prices could print in the format of $dollars with two spaces adter the decimal point.

![image](https://github.com/user-attachments/assets/8d7ae07d-3d08-4e8b-91d1-357604a45786)

![image](https://github.com/user-attachments/assets/cebf31da-25dd-4a53-af29-07951261bb85)

## Tweaks

At this point, my script was finished, however I was missing two points:
- The script is supposed to tell the user how much money they have left after each order is made and
- the user's final budget is shown to them after they agree to pay 

to fix the first issue, I just added in a print statement to print each price from the menu based off the order - right after the print statement for outputting the mealTab list. 
![image](https://github.com/user-attachments/assets/47685672-724b-47e3-a6ef-601314e00f29)

This successfully printed the price of the latest added item into mealTab.

![image](https://github.com/user-attachments/assets/835d2011-5aa0-43be-bcef-bdbef30d92ee)


To fix the latter issue, I moved the print statement of showing the remainingBudget into the if statement that checks if the user's answer is yes. Similarly to my order while loop, I nested this if statement into a while loop so that I could have the "are you paying for the meal?" prompt appear again if a user typed in something other than y or n. 

Then for the **challenge**, I nested another if statement that checks if the user says yes. Here I have if remainingBudget < 10, as in the user only has $10 left of their budget, the date takes that as a compliment of sacrifice and agrees to a second date. if remainingBudget > 10, then the date doesn't think the user spent enough and is not interested in another date. Lastly, I used another elif clause to say if remainingBudget < 0, then they have to go and wash dishes and no second date. 

![image](https://github.com/user-attachments/assets/1cf79c14-df90-4b58-877a-f9e803e9375a)

testing didn't work and I realized I Ran into the same issue as before. I switched the elifs around and had the first if condition check if remainingBudget < 0 instead. Tested out all the different combinations and each print statement worked as intended.

![image](https://github.com/user-attachments/assets/41ddf010-3a98-448c-bdcb-e34f386253f6)

## Menu
I updated the menu we made in groups to have a price for each item. 

I made sure to type cast the budget to be a float when saving it to ensure that it was saved as a decimal point number. 




## Challenge
For the challenge, if the user chooses to *both* pay for the meal and doesn't pick one of the meals the date dislikes, they will get a second date. I decided that the date would automatically strongly dislike 
ordering an appetizer because they believe in getting to the entree fast.

If the user doesn't offer to pay for the date, they will not get a second date. Also if they offer to pay, but have insufficient funds, the date will leave and will not be open to a second date. 

## Style Edits

I added in input lines to read the user's name so I could use it in various prompts.  
Later, I added in style edits such as a menu title: "Python Palace" and a line of '~' to frame the end od the menu. To show uniform spaces between the food and the prices, I also added in a 10 after key in `print(f"{key:10}: ${value:.2f}")`.

![image](https://github.com/user-attachments/assets/6710e02e-450a-4e24-aaad-c18c8227fc61)

![image](https://github.com/user-attachments/assets/5dc0e05e-f49b-4da5-b4da-b7866ff49435)

**Date Simulation**
After the user has finished all orders, I included a print command to say "Enjoy eating!" and a sleep command to simulate the date. The sleep equivalent in Python I found was time.sleep(), but I had to install the time command. 
