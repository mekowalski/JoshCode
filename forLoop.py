# create a passcode checker
# if passcode contains an invalid character, print the invalid symbol

# passcode = input("please enter passcode: \n")
# invalid = "!@#$%^&*()_+?><"

# for character in passcode:
#     if character in invalid:
#         print("this character is invalid:", character)
        
        
# create program to count vowels in a word
# take an input for a word
# loop through the work and check for vowels
# at the end, print off number fo vowels in the word

# word = input("please enter a word: ")
# vowels = "aeiou"
# vowelCount = 0

# for letter in word:
#     if letter in vowels:
#         vowelCount +=1
# print("your word had this many vowels: ", vowelCount, "\n")


# create a phone number checker
# if the variable contains anything but a number print "invalid phone number" and exit loop

# phoneNumber = input("Enter your number, no spaces please: \n")
# numbers = "0123456789"

# for number in phoneNumber:
#     if numbers not in numbers:
#         print("that is not a valid number \n")
#     elif phoneNumber in numbers:
#         print(phoneNumber)
# print("Thank you!")


# use range function
# create program taking number of guests
# for each guest ask their name and age
# if guest is 18+ YO, welcome user
# otherwise tell them they must be 18 to drink

guests = int(input("Please enter number of guests: "))

for guest in range(guests):
    name = input("Please enter your name: ").capitalize()
    age = int(input("Please enter your age: "))
    if age >= 18:
        print(name, "Welcome to the bar! \n")
    else:
        print("You must be 18+ years old to drink! \n")
print("goodbye")