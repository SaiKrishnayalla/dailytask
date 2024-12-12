# union of sets
set_1 = {'sun','mon','tue','wed'}
set_2 = {'thursday','friday','saturday'}
print("union:" , set_1.union(set_2))

#intersection of sets
set_1 = {1,2,3,4,5,6,7}
set_2 = {8,9,10,11,12,1,2,3}
print("intersection:", set_1.intersection(set_2))

#differenciate of sets
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print("Difference:" , Days1.difference(Days2))

#symmetric difference of set
a = {1,2,3,4,5,6}  
b = {1,2,9,8,10}  
c = a.symmetric_difference(b)
print(c)  