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

# not sure if i should ask user to start with state or activity type?
# how do i implement for loop? use id for difficluty level? use it for state options? use it for activity type?
# for state in stateoption
    # if state == NM
        # have difficulty level entered
        # then print the difficulty level activity at the location of chosen state

# OR
# for level in difficultylevel
    # if level == 1
        # have state entered
        # then print difficulty level activity at location of chosen state

# OR
# for activity in activitytype
    # if activity == 1
        # 

enter = input("Enter 1-Start or 2-Stop: ")
while enter == "1":
    activityType = int(input("Enter Activity Number: 1-Hiking, 2-Biking, 3-Water Day :"))
    if activityType == 1:
        stateOption = input("Enter State for Activity: CO, NM, UT, AZ : ").upper()
        print("Great you chose", stateOption, "\n")
        level = input("Difficulty Level:  1-Easy, 2-Hard :")
        
        # maybe two conditions should be met: if state == NM and level == 2
            # then print("you can do a hard hike in NM at atalaya mountain trail in santa fe!")
            # there would be 8 options for hiking alone, 4 states X 2 levels
        if stateOption == "AZ" and level == "1":
            print("You can do an easy hike in", stateOption, "at West Fork Trail in Sedona. \n")
        elif stateOption == "AZ" and level == "2":
            print("You can do a hard hike in", stateOption, "at Camelback Hike in Phoenix. \n")
        elif stateOption == "CO" and level == "1":
            print("You can do an easy hike in", stateOption, "at Falls Creek Meadows in Durango. \n")
        elif stateOption == "CO" and level == "2":
            print("You can do a hard hike in", stateOption, "at Black Bear Pass Trail in Telluride. \n")
        elif stateOption == "NM" and level == "1":
            print("You can do an easy hike in", stateOption, "at Pueblo Loop Trail at Bandelier National Monument. \n")
        elif stateOption == "NM" and level == "2":
            print("You can do a hard hike in", stateOption, "at Wheeler Peak in near Toas. \n")
        elif stateOption == "UT" and level == "1":
            print("You can do an easy hike in", stateOption, "at Zion Canyon Overlook near Hurricane . \n")
        else:
            print("You can do a hard hike in", stateOption, "at Hidden Valley Trail near Moab. \n")
            
            # should i just move onto new project? this is just getting long and tedious -_-
            
            
        
    elif activityType == 2:
        print("you chose biking! \n")
        stateOption = input("Enter State for Activity: CO, NM, UT, AZ : ").upper()
        if stateOption == "AZ":
            print("You can bike an EASY trail in", stateOption, "at Bell Rock Pathway in Sedona \n")
            print("OR \n")
            print("You can bike a HARD trail in", stateOption, "at Mt Lemmon near Tucson \n")
        elif stateOption == "CO":
            print("You can bike an EASY trail in", stateOption, "at Red Rocks Canyon Open Space in Colorado Springs \n")
            print("OR \n")
            print("You can bike a HARD trail in", stateOption, "at Horsehoe Trail near Canyon Creak Area \n")
        elif stateOption == "NM":
            print("You can bike an EASY trail in", stateOption, "at Galisteo Bason Preserve in Santa Fe \n")
            print("OR \n")
            print("You can bike a HARD trail in", stateOption, "at Alien Run Trail in Aztec \n")
        else:
            print("You can bike an EASY trail in", stateOption, "at Round Valley's Big Easy Trail in Park City \n")
            print("OR \n")
            print("You can bike a HARD trail in", stateOption, "at Porcupine Rim in Moab \n")
        # just for myself, print an easy and hard biking trail once state is selected
    else:
        print("you chose a water day!")
        # same here, just give both free/fee options in the chosen state

    break
