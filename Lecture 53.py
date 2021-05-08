def VAT(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print(VAT(float(input("Enter Your Price : "))))