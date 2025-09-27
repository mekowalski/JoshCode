def grade(percentage):
    print("Enter your grade percentage: ")
    if percentage > 0 and percentage <= 50:
        print("IMPROVE YPUR GRADE!!!")
    elif percentage > 50 and percentage <= 70:
        print("You're barely passing the class")
    elif percentage > 70 and percentage <= 90:
        print("You're doing great! Keep it up!")
    else:
        print("You're top tier!")

percentage = int(input("Please enter your grade percentage: "))
grade(percentage)