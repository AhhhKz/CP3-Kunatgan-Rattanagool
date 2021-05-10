def login():
    username = input("Enter Your Username : ")
    password = input("Enter Your Password : ")
    if username == "admin" and password == "1234":
        return True
    else:
        return False
def showmenu():
    print("-------------Godlike Shop------------")
    print("-----Press number to Select Menu-----")
    print("Press 1 VAT Calculator")
    print("Press 2 Price Calculator")
def Menu():
    UserSelected = int(input("Select to "))
    return UserSelected
def VAT(totalprice):
    vat = (totalprice * 7 / 100)
    result = totalprice + vat
    return result
def Price():
    price1 = int(input("Enter price1 : "))
    price2 = int(input("Enter price2 : "))
    return VAT(price1 + price2)

if login() == True :
    showmenu()
    if Menu() == 1:
        print(VAT(int(input("Enter Your Price : "))))
    else:
        print("Total price :",Price())
else:
    print("Wrong Username or Password")