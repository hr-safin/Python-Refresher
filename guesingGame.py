# guesing game

sectret_number = 9
guess_count = 0
guess_limit = 4

while guess_count < guess_limit:
    guess = int(input("Guess"))
    guess_count += 1

    if(guess == sectret_number):
        print("You won")
        break

else:
    print("sorry you failed try again")


