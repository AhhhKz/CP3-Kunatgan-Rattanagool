menu = []
def showBill():
    print("MyFood".center(33,"-"))
    priceTotal = 0
    for num in range(len(menu)):
        priceTotal += int(menu[num][1])
        print(menu[num][0].ljust(25," "),menu[num][1].rjust(3," "),"THB")
    print("Total Price".ljust(25, " "), str(priceTotal).rjust(3, " "), "THB")
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.casefold() == "exit":
        print("Success to enter order")
        break
    else:
        menuPrice = input("Price : ")
        menu.append([menuName,menuPrice])
showBill()

