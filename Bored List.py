exit = False
while exit == False:
    print('what do you want to do?\n'
            'Add?\n'
            'Check?\n'
            'Clear?\n'
            'Exit?')
    inpt = input()
    if inpt == "Exit":
        print("Exited")
        exit = True
    elif inpt == "Add":
        print("what do you want to add?")
        while True:
            todo = input()
            if todo == 'Exit':
                break
            else:
                with open('To-Do list', "a+") as List:
                    List.write(todo + "\n")
    elif inpt == "Check":
        with open('To-Do list', "r") as rList:
            print(rList.read())
    elif inpt == "Clear":
        with open('To-Do list', "w") as wlist:
            wlist.write("")

ds-lkjnkfdu
