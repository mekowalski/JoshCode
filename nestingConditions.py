# gather a rating of 1-10 from customer/user
# if rating is 9 and above, state thank you so much
# if rating is less than 9 and more than 5, ask how they can improve
# print of the inout and add we will work harder and better
# any other rating, state we are sorry to hear that

rating = int(input("How do you rate this from 1-10, 1 = lowest, 10 = highest: \n"))

if rating >= 9:
    print("THANK YOU SO MUCH!!!")
elif rating >=5 and rating <=9:
    improve = input("How can this improve: \n").capitalize()
    print("You said:", improve)
    print("We will work harder and better!")
else:
    print("We are sorry to hear that and will work on this!")