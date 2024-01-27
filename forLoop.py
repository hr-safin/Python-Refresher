# name = ["hasibur", "mahi"]

# for x in name:
    # print(x)

# range has 3 parameter 1.starting index (inclusive) 2.ending index (exclusive) 3. increment (by default 1)
# for x in range(0,6,2):
    # print(x)

# first solution
total = 0
price = [10, 20, 30]

for i in price:
    total += i
print(f"The total is : {total}")

# second solution

total2 = 0
price2 = [10,40,50]

for j in range(len(price2)):
    total2 += price2[j]
print(total2)