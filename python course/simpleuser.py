game_list1 = [
    {'row1' :[' ',' ',' ']},
    {'row2':[' ',' ',' ']},
    {'row3':[' ',' ',' ']}
]
        

def display(game_list1):
    print ('Here is the game [sudUku]: ')
    print(game_list1)
def user_choice():

    choice1 ='126'
    while  choice1  not in ['row1','row2','row3']:
        choice1 = input('enter a row from(row1,row2,row3): ')


        if  choice1 not in  ['row1','row2','row3']:
            print ('please! enter a valid row')
        else:
            break
    return choice1

def position_choice1(game_list1,position):

    res = [x for x in game_list1 if position in x]

    my_result = (res[0])

    my_list = (input("choose a number('0','1','2'):  "))

    for key,value in my_result.items():
        value[1] = my_list

    print(my_result)

def game_over ():

    choice1 = ''
    while  choice1  not in ['Y','N']:
        choice1 = input('Do you want to continue the game or quit ? ' "enter 'Y' OR 'N': ")

        if choice1 not in ['Y','N']:
            print('please enter a valid option: ')

        elif choice1 == 'Y':
            return True 

        else:
            return False 
    

#gameon = True

#while gameon:
#    display()
#    replaced = user_choice()
#    game_list1= position_choice1(game_list1,replaced)
#    gameon = game_over()

#games_lists = [display]

#def home():
#    print('choose the game you want to play from the below: \n ')
    
#    print ('values filling game')
#    print ('sudUku')

#home()




gameon = True

while gameon:
    display(game_list1)

    position  = user_choice()
    

    game_list1 = position_choice1(game_list1,position)


    gameon = game_over()

    
    if gameon == True:
        continue
    else:
        break



'''game_list1 = [
    {'row1' :[' ',' ',' ']},
    {'row2':[' ',' ',' ']},
    {'row3':[' ',' ',' ']}
]
    step 1 -select row1
    step 2 -please enter the value you want to see in row1 - 0
    step 3 - value should be represented in row1
    
    {'row1' :['0 ',' ',' ']},
    {'row2':[' ',' ',' ']},
    {'row3':[' ',' ',' ']}
    step 4 - do you want to continue the match - Y or N 
'''