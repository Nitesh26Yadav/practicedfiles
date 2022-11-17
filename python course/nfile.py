game_list1 = [
    {'row1' :[' ',' ',' ']},
    {'row2':[' ',' ',' ']},
    {'row3':[' ',' ',' ']}
]

position = 'row3'
res = [x for x in game_list1 if position in x]


my_list=(res[0])
 

for key,value in my_list.items():
    value[1]=2
    

print(my_list)





























#res +[0]
#print(type(position))
#print(res)
#res.insert(1,1)
#print(res)

#res[0][1]='2'
#print(res)

#print(res+[1])

