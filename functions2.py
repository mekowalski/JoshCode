# def grade(percentage):
#     if percentage > 0 and percentage <= 50:
#         print("IMPROVE YOUR GRADE!!!")
#     elif percentage > 50 and percentage <= 70:
#         print("You're barely passing the class")
#     elif percentage > 70 and percentage <= 90:
#         print("You're doing great! Keep it up!")
#     else:
#         print("You're top tier!")

# percentage = int(input("Please enter your grade percentage: "))
# grade(percentage)

# def bankBalance(balance):
#     if balance >= 500:
#         return True
#     else:
#         return False

# name = input("Please enter your name: ").capitalize()
# balance = float(input("Please enter your current balance: "))

# res = bankBalance(balance)
# if res == True:
#     print("Your balance is above $500. You have enough funds \n")
# else:
#     print("Your balance is below $500. Bank balance is low \n")
    
def mortgage(deposit):
    if deposit >= 50000:
        print("You're Approved!!! \n")
    elif deposit >= 20000 and deposit < 50000:
        print("You need an approval process. \n")
    else:
        print("Not approved for a mortgage. \n")
        
name = input("Enter name: ")
deposit = int(input("Enter deposit: "))
totalAmount = 0
while deposit != 0:
    totalAmount += deposit
    mortgage(deposit)
    deposit = int(input("Deposit amount: "))
print("Total amount requested: ", totalAmount)
    
