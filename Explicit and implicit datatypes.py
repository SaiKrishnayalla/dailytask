#imlicit type conversion 
# the data type of a variable is changed to match te value assigened to it
# it will return the vale without the loss of data 
int_Num = 10
int_float = 22.4
print(type(int_Num))
print(type(int_float))

new_Number = int_Num+int_float

print(type(new_Number))
print(new_Number)


#Explicit data type conversion.
#this is type casting method because we are casting the type of variable to a different type
#in this method we have to specify the type of data that we wan to convert to
# we loss some data in this method
int_num = 5
int_float = 10.5
print(type(int_num))
print(type(int_float))
# we are converting int_num to float
print("________________________")
float_num = float(int_num)
print(type(float_num))
print(float_num)
int_str = int(int_float)
print(type(int_float))
print(int_str)