# positonal
def function(a,b,c,d):
    return a,b,c,d
a = 10
b = 20
c = 30
d = 40
print(function(c,a,d,b)) # whatever the position we are passing in arguments that will print accordingly




# key word arguments
def function(a,b,c,d): # here a,b,c,d are key word arguments
    return a,b,c,d
print(function(b=20,c=10,a=5,d=1)) #it will print order of parameters



#default arguments
def default_arg(a=10,b=20): # here a,b are default arguments
    return a,b
print(default_arg(1)) # here 1 is assigned to a and 20 is assigned to b
print(default_arg(b=11)) # here 10 is assigned to a and 11 is assigned to b


# variable length
def vamsi(*args):
    return args
print(vamsi(1,2,3,4,5,1,2,2,3,1,2,2,1,2,1,2,1,2,1,2,2,1,2,1,2,1,2,1,2,1,2,1,1,21,2,2,1,2,2)) # by using *args we can pass any number of arguments

# we can also use **kwargs for keyword arguments
def vamsi(**kwargs):
    return kwargs
print(vamsi(a=1,b=2,c=3,d=4,e=5,))
# we can also use *args and **kwargs together
def vamsi(*args,**kwargs):
    return args,kwargs
pass

# key word variable length