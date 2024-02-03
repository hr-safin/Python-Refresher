command = ""
started = False
while  True:
    command = input("> ").lower()
    if(command == "start"):
        if(started):
            print("Car is already started")
        else:
            started = True
            print("Car starting")

    elif(command == "stop"):
        if(not started):

            print('Car is already stopped')
        else:
            stopped = False
            print("Car stopped")
    elif(command == "help"):
        print('''
start -- to start the game
stop -- to stop the game
quit -- to quite the game
        ''')
    elif(command == "quit"):
        break
    else:
        print("Sorry, I don't understand")
