name="sami"
print(name)

print("hello", name, sep="~")

apple="he said, \"my name is apple\""  
apple1='he said, "my name is apple"'
                                             #printing double quotation in a string using \"   
print(apple)
print(apple1)

a=len(apple)                                  #finding the length of string
print(a)


for char in name:
    print(char)


print(name[0:4])
print(name[-4:])
                                                ### Methods in string

a="my name is sami"
a=a.upper()
b=a.lower()
print(a)
print(b)

ab="samiieeeeeeeee"
print(ab.rstrip("e"))
print(ab.replace("e","!"))
print(a.split())
print(a.capitalize())
print(a.count("SAMI"))
print(a.isspace())



