thisList = ["apple","banana", "watermelon"]

print(thisList)
print(thisList[-1])
print(thisList[1:])
print(thisList[0:2])
thisList.pop(2)
print(thisList)

thisList.append("mango")
print(thisList)


# find the largest number

numbers = [3,4,5,7,10]
max_number = numbers[0]

for number in numbers:
    if(number > max_number):
        max_number = number

print(max_number)

# find the smallest number

number2 = [23,4,5,69,0,-1,8]
min_number = number2[1]


for number in number2:
    if(number < min_number):
        min_number = number

print(min_number)

# reverse the list

firstList = ["peyara","mango","bob", "apple", "cat"]

firstList.sort()
print(firstList)