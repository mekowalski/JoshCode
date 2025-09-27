def personInfo(name, age, nationality):
    print("Welcome:", name "\n")
    print("You are:", age "\n")
    print("You are:", nationality "\n")
    
number = int(input("Amount: "))
for i in range(number):
    name = input("Enter first name: ").capitalize()
    age = input("Enter your age: ")
    nationality = input("Enter your nationality: ").capitalize()
    personInfo(name, age, nationality)