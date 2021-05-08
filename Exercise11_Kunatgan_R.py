Num = int(input("Enter Num : "))
text = " "
i = 1
for x in range(Num):
    print(text*(Num-x),"*"*i,text*(Num-x))
    i += 2