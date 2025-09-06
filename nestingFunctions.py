# shorten code into nested functions(refactor)

# code 1
# rentalPrice = int(input("Car Price/Day: "))
# rentalDays = int(input("Days of Rental: "))
# total = rentalPrice * rentalDays
# print("Total Rental Price: $", total, "\n")

# code 2
# package1 = int(input("Enter 1st package weight: "))
# package2 = int(input("Enter 2nd package weight: "))
# package3 = int(input("Enter 3rd package weight: "))
# total = (package1 + package2 + package3) * 0.6
# print("Shipment total: $", total)


# code 3
'''create expense tracker
collect user's income
collect expenses for food, rent, phone bill, internet, utilities
suggest amount of savings from remaining
get total amount after expenses, print remaining total and savings total'''
income = int(input("Enter monthly income: "))
rent = int(input("Enter monthly rent: "))
groceries = int(input("Enter monthly groceries: "))
phoneBill = int(input("Enter phone bill: "))
internet = int(input("Enter internet bill: "))
utilities = int(input("Enter monthly utilities: "))
monthlyRemaining = income - (rent + groceries + phoneBill + internet + utilities)
print("Your monthly remaining amount: $", monthlyRemaining, "\n")

suggestedSavings = monthlyRemaining * .15
print("Consider adding 15% of your remaining balance of", suggestedSavings, "to a savings account :) \n")


# code 4
'''create overtime tracker
collect user's monthly pay
collect user's extra hours worked
their bonus is 20% of monthly pay * extra hours worked
print overtime total'''
# monthlyIncome = int(input("Enter monthly income: "))
# extraHours = int(input("Enter overtime hours: "))
# overtimeAmount = (monthlyIncome * 0.2) * extraHours
# print("Total Overtime Amount: $", overtimeAmount, "\n")