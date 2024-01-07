weight = int(input("Enter Your weight "))
unit = input("(L)bs or (K)ilos ")

if(unit.upper() =="L"):
    converted = weight * .45
    print(f"The weight is {converted} kilos")
else:
    converted = weight / .45
    print(f"The weight is {converted} pound")