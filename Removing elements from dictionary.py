#pop
dict = {"Name": "vamsi", "Age":22, "city":"Hyderabad", "country": "india"}
dict.pop("Age")
print(dict)

#del()
dict = {"Name": "vamsi", "Age":22, "city":"Hyderabad", "country": "india"}
del dict["Age"]
print(dict)

#deleting entire dictionary
dict = {"Name": "vamsi", "Age":22, "city":"Hyderabad", "country": "india"}
del dict 
print(dict)

#clear()
dict = {
    "Name":"YVN",
    "Age":22,
    "city":"hyd"
}
dict.clear()
print(dict)

#pop item
dictionary = {
    "Owner" : "YVN",
    "brand":"BMW",
    "Model" : "x7",
    "Year" : 2022
}
dictionary.popitem()
print(dictionary)



dictionary = {
    "Owner" : "YVN",
    "brand":"BMW",
    "Model" : "x7",
    "Year" : 2022,
    "insurance" : "yes"
}
dictionary.popitem()
print(dictionary)