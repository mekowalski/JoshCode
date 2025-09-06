# create a mini message bot that accepts messhage
# the loop breaks/ens when the word "done" is entered and print how many messages were left
# everytime the loop runs, print "we got your message"

# message = input("Please enter your message(enter 'done' to exit): ")
# totalMessages = 0
# while message != "done":
#     totalMessages += 1
#     print("We got your message. \n")
#     message = input("Next message: \n")
# print("You wrote us", totalMessages, "messages.")
    
    
# create login account
# user has 2 passwords and either can be used for access
# once a correct password i entered, state welcome to your account

passcode = input("Please enter passcode: ")
while passcode != "july30" and passcode != "954375":
    passcode = input("That was incorrect, please try again: ")
print("Welcome to your account")
