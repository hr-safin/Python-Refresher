is_hot = False
is_cold = False

if (is_hot):
    print("Its a hot day")
    print("Drink plenty of water")
elif (is_cold):
    print("Its a cold day")
    print("Wear worm cloth")

else:
    print("It is fall enjoy your day", "Lovely day")


price = 1000000
has_good_Credit = False


if (has_good_Credit):
    down_payment = .1 * price

else:
    down_payment = .2 * price


print(f"${down_payment}")


mark = 70

if (mark >= 70):
    print("A+")
elif (mark < 70):
    print("A")
else:
    print("B")