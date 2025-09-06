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
# once state is entered, i'm asking user about difficluty level but how do i keep stateOption?
# i don't want it to print an actiivity with a difficulty level for NM when CO was entered


hiking = 1
biking = 2
waterDay = 3

enter = input("Enter 1 :Start or 2 :Stop ")
while enter != "2":
    activityType = input("Enter 1 :Hiking, 2: Biking, 3 :Water Day :")
    if activityType == "1":
        stateOption = input("Enter State for activity: CO, NM, UT, AZ: ")
        print("Great you chose", stateOption, "\n")
        level = input("Enter 1 :Easy, 2 :Hard :")
        
        # if 1easy then show easy hiking place
        if level == "1":
            print("Okay!  You can do an easy hike in", stateOption, "at Falls Creek Meadows in Durango CO. \n")
        # else 2 hard then show hard hiking place
        else:
            print("Okay! You can do a hard hike in", stateOption, "up Engineer Mountain in the San Juan Mountains. \n")
    # elif 2:
        # stateOption
    # else 3:
        # stateOption
        # print("you chose state: ", stateOption)
    break
        
    # print("yay we're here!")
    # break