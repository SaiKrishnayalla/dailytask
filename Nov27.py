# write a python program to find the mid value of a string 
x=input("Enter a string to find mid value:")
print(len(x)//2)

# write a python program to a digit without using isdigit() function
x=input("Enter a digit:")
if ord(x)>=48 and ord(x)<=56:
    print("x is digit")
else:
    print("x is not a digit")

# write a python program to find the last occurance of a  vowel in a string and replace it with a '-'.
n1 = input("Enter the  string to replace vowel occurance with -: ")
vowels ='aeiouAEIOU'
for k in n1:
        if k in vowels:
            n1 = n1[::-1].replace(k,'-', 1)[::-1] # Replace last occurrence of vowel
            break  # Exit the loop after replacing the first vowel
print(n1)