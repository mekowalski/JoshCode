'''
STRUCTURE:
Input statement to start program
Main While Loop(repeat until an event)
Conditional Statements(if/elif/else)
print()duh
Try adding for loop
5 or more main actions
Nesting is KEY!
*50 lines minimum*
'''

# activity type: hiking, biking, water day
# once entered, ask for which type of activity(with numbers?)
# hiking = 1, biking = 2, waterday = 3
# if activitytype == 1 then go into hiking options and etc for 2 and 3

# activity type
# state option
# hiking: easy, hard
# biking: easy, hard
# water day: free, fee


hiking = 1
biking = 2
waterDay = 3

enter = input("Enter 1 :Start or 2 :Stop ")
while enter != "2":
    activityType = input("Enter 1 :Hiking, 2: Biking, 3 :Water Day :")
    if activityType == "1":
        stateOption = input("Enter State for activity: CO, NM, UT, AZ: ")
        print("you chose state: ", stateOption)
    break
        
    # print("yay we're here!")
    # break