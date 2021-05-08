user = input("Enter Your Username :")
password = input("Enter Your Password :")
Cocacola_Str = "Cocacola"
Cocacola = 25
Chocolate_Str = "Chocolate"
Chocolate = 50
Latae_Str = "Latae"
Latae = 60
Capucino_Str = "Capucino"
Capucino = 60

if user == "Kunatgan" and password == "0909160974" :
    print("Log in Complete !!")
    print("")
    print("--Welcome to Godlike_Shop--")
    print("------------Menu-----------")
    print("1.",Cocacola_Str,"       ",Cocacola,"THB")
    print("2.",Chocolate_Str,"      ",Chocolate,"THB")
    print("3.",Latae_Str,"          ",Latae, "THB")
    print("4.",Capucino_Str,"       ",Capucino, "THB")
    print("press to select menu")
    Userselectedmain = input("Select Choice (y or n)")
    if Userselectedmain == "y":
        Userselected1 = int(input("Select Cocacola amount :"))
        Userselected2 = int(input("Select Chocolate amount :"))
        Userselected3 = int(input("Select Latae amount :"))
        Userselected4 = int(input("Select Capucino amount :"))
        Sum = (Userselected1 * Cocacola) + (Userselected2 * Chocolate) + (Userselected3 * Latae) + (Userselected4 * Capucino)
        print("Total Order Price =",Sum,"THB")
        print("Success to Order")
    elif Userselectedmain == "n":
        print("Success to Order")

else:
    print("Wrong Username or Password !")