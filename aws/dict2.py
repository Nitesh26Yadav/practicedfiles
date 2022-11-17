from collections import Counter
 
# initializing two dictionaries
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400, 'e':500}
 
 
# adding the values with common key
         
Cd3 = Counter(d1) + Counter(d2)
print(Cd3)