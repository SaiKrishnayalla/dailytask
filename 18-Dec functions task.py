#1.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"
def greet(name):
    print (f"Hello,  { name }  !")
greet("Vamsi")

 
#2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.
def add_numbers(a, b):

    return(a + b)
print(add_numbers(10 ,20))



#3.Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    # Test the function with a number
print(is_even(10))

#4.Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).





#5.Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.
def find_max():
    a=10
    b=20
    c=300
    return max(a,b,c)
print(find_max())






#6.Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.
def count_vowels():
    vowels = 'aeiou'
    while True:
        s = input("Enter a string: ")
        count = 0
        for char in s:
            if char in vowels:
                count += 1
print(f"The string '{s}' contains {count} vowels.")


#7.Create a function `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise.





#8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).





#9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the two numbers and return the result.






#10.Write a function `find_common_elements` that takes two lists as input and returns a list of elements that are present in both lists.
def find_common_elements():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    return [value for value in list1 if value in list2]
print(find_common_elements())



#11.Write a function `reverse_string` that takes a string as input and returns the string reversed.
def reverse_string(s):
    return s[::-1]
s= reverse_string("skywaves")
print(s)
 
#12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples sorted by the dictionary values in ascending order.
