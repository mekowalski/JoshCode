# def personInfo(name, age, nationality):
#     print("Welcome:", name, "\n")
#     print("You are:", age, "\n")
#     print("You are:", nationality, "\n")
    
# for i in range(2):
#     name = input("Enter first name: ").capitalize()
#     age = input("Enter your age: ")
#     nationality = input("Enter your nationality: ").capitalize()
#     personInfo(name, age, nationality)

def goodDeal(cost):
    if cost >= 60 and cost < 120:
        response = "This is a great deal!"
    elif cost >= 120:
        response = "This is 'tlai-a'!"
    else:
        response = "This is cheap! BUY NOW"
    return response

store = input("Enter your store name: ")
cost = int(input("Item price: "))
res = goodDeal(cost)
print(store, "-", res)
if res == "This is a great deal!":
    print("Buy before it's too late!")