#  Random Guess number Game
import random
 # import the random libary
Your_number=int(input("Enter Your NUmber:")) 
#this code for user enter here number
Rupees=int(input("Add your Amount(₹):")) 
#insert your amount in ₹
x=int(input("Amount growth rate(using only 1-10):"))
rand=random.randint(1,10)
# use the random.randint function for guess the number
if(x>10):
    print("Please enter value in range")
    y=int(input("Amount growth rate(using only 1-10):"))

    

print(f"Random Number :{rand}")
#this code line use for print random number

#given a condition for winner and looser in the game
if(Your_number==rand):
    print("You are Winner //")
    print(f"Win You are Prices{Rupees*x}")# if the user are win the here amount grow insert the x_rate
else:
    print("You are losser!")#if user are loss the game then print her condition
    print(f"YOU ARE LOSS THE AMOUNT(₹{Rupees})")

    # it is note and part of code 
print("THIS IS GAME GET CHILL & ENJOY")
# repeat the process
print("TRY AGAIN ?")

