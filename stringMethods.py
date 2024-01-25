#string method
# string is immutable we cannot change directly any strings

name = '  hasibur rahman safin  '
name2 = 'HASIBUR RAHMAN SAFIN'

print(name.upper())
print(name.lower())
print(name.strip())
name3 = name.split()
print(name3)  #split into word and create array

name = " ".join(name3)
print(name)

print(name.find("h"))
print(name.replace("hasibur", "mahi"))