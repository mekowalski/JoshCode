# create a program to recomment a type of trip to the user
# gather trip cost from the user
# if cost is >= 350, go for stay-cation
# if cost is <= 350 and <= 1000, go for a roadtrip
# if cost is > 1000, go for flight to the beach

# print("Let me recommend the type of vacation you should have based on your price: \n")
# tripPrice = int(input("What is your budget? "))

# # conditional
# if tripPrice < 350:
#     print("you should go camping or have a stay-cation!")
# if tripPrice >= 350 and tripPrice <= 1000:
#     print("you could go on a cool roadtrip!")
# if tripPrice > 1000:
#     print("you should catch a flight to the beach!")
    
    
# create a variable thath  holds a 6digit pin/password
# if pin is correct, state "welcome back"
# else state "incorrect try again"

# pin = int(input("what is your 6-digit pin: \n"))
# # conditional
# if pin != "945375":
#     print("Incorrect pin")
# else:
#     print("Welcome back! \n")


# allow user to enter special discount code
# if discount code is equal to summer25 then give 25% off
# otherwise day the code is not valid

# discountCode = input("Enter Discount Code: \n").lower()
# discount = discountCode == "summer25"
# print("You get 25% off: ", discount)

# conditional
# if discountCode == "summer25":
#     print("You get 25% off! \n")
# else:
#     print("Discount Code is Invalid \n")
    

# create a latte for user
# ask if they want regular or blonde espresso
# ask if they want milk or oatmilk
# ask if they want sweeteners: brown sugar, salted maple syrup, chocolate or none
# based on selection suggest a type of latte

espresso = input("Regular or Blonde Espresso: \n")
milk = input("Whole Milk or Oatmilk: \n")
sweetener = input("Sweeteners: Salted Maple Syrup, Chocolate or None: \n")

regularLatte = espresso == "regular" and milk == "whole milk" and sweetener == "none"
blondeLatte = espresso == "blonde" and milk == "whole milk" and sweetener == "none"
upstateNYLatte = espresso == "regular" and milk == "oatmilk" and sweetener == "salted maple syrup"

if regularLatte:
    print("You ordered an unsweetned regular latte!")
if blondeLatte:
    print("You ordered an unsweetened blonde latte!")
if upstateNYLatte:
    print ("You ordered an Upstate New York Latte!") 
