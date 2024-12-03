#pop
fruits=['apple','orange','kiwi']
x =fruits.pop(1)
print(x)

#clear()
fruits=['apple','orange','kiwi']
fruits.clear()
print(fruits)

#remove
x=[1,2,3,4,5,6,7,8,9,10]
x.remove(5)
print(x)

#reverse
list = [0,1,2,3,4,5,6,7,8,9]
list.reverse()
print(list)

#delete
x=[1,2,3,4,5,6,7,8,9]
del x[2]
del x[2:5]
print(x)
print(x)

#reverse a string using slicing
s="hello world"
print(s[::-1])

#sort
numbers = [7,3,1,2,8,6,5,4,9]
brands = ['Merdidies','BMW','Range rover','Ducati']
brands.sort()
print(brands)
numbers.sort()
print(numbers)

#alias
a =[1,2,3]
b=a
b[0] = 10
print(a)

#cloning


#nested list
nested_list = [1,2,3[4,5,6]]
print(nested_list[1])
