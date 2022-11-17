def user_choice():

    choice = 'name'

    while choice.isdigit() == False:
        
        choice = input('choose a number : ')


        if choice.isdigit() == False:
            print("sorry! wrong input")

        return int(choice)

print(user_choice())

