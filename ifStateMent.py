age = int(input("Enter your age please "))

if(age > 18):
    print("You are eligable for this website")

else:
    print("You are not eligable for this website")



# discounted price

billAmount = int(input("Enter your bill amount"))

if(billAmount > 50):
    discounted = billAmount - (billAmount / 10)
    print(f"The discounted bill is : {discounted}")

elif(billAmount > 20 and billAmount < 50):
    discounted  = billAmount - (billAmount / 5)
    print(f"The discounted bill is : {discounted}")

else:
    print("No Discount")