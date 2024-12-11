#assigning multiple elements to a single variable
#packing
#packing and unpacking using tuples
my_pack = (1,2,3,4,5)
print(my_pack)
print(type(my_pack))

#unpacking
my_pack =(1,2,3,4)
a,b,c,d = my_pack
print(a)
print(b)
print(c)
print(d)
print(a,b)

#extended unpacking
#using * we can assign multiple attributes
a,b,*rest =my_pack
print(a)
print(*rest)