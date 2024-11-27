#2Python program to check a String is palindrome or not. 
string=input(("Enter a letter:"))  
if(string==string[::-1]):  
      print("The letter is a palindrome")  
else:  
      print("The letter is not a palindrome")

#7.Python program to convert lowercase vowel to uppercase in string
string =input("Enter a string")
y=string.replace("a","A").replace("e","E").replace("i","I").replace("o","O").replace("u","U")
print(y)

#16. Python program to count the Occurrence Of Vowels & Consonants in a String. 
x = "learning python is easy"
vowels = "aeiou"
consonents = "bcdfghjklmnpqrstvwxyz"
x1=sum(x.count(vowels)for vowels in vowels)
x2=sum(x.count(consonents)for consonents in consonents)
print()
print(x1)

#15. Python program to delete vowels in a given string.
string ="hello world"
y=string.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
print(y)