def user_choice():
    choice = 'name'
    choice.isdigit()==False
    within_range = False

    while choice.isdigit()==False or within_range ==False:
        choice = input('choose a number (0,10): ')

        if choice.isdigit() == False:
            print('sorry! wrong input')

        if choice.isdigit()== True:
            if int(choice) in range (0,10):
                within_range = True

            else:
                print ('sorry out of range')
                
    return int(choice)

print (user_choice())

             