menu = []
price = []
def showBill():
    print("MyFood".center(33,"-"))
    priceTotal = 0
    for num in range(len(menu)):
        priceTotal += int(price[num])
        print(menu[num].ljust(25," "),price[num].rjust(3," "),"THB")
    print("".center(33, " "))
    print("Total Price".ljust(25," "),str(priceTotal).rjust(3," "),"THB")
    print("".center(33, "-"))
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.casefold() == "exit":
        print("Success to enter order")
        break
    else:
        menuPrice = input("Price : ")
        menu.append(menuName)
        price.append(menuPrice)
showBill()

