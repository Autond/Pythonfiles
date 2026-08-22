str= "ABCAcademy.com"
str1= "Consulting firm"
str3= "ABC"

print(str[1])
print(str[0:3])  # substring in python
print(str+" "+str1) # concatenation

print(str3 in str) # substring check

var= str.split(".")  # to split the string
print(var)
print(var[0])

str4= "   great  "
print(str4.strip())  # to strip the whitespaces

print(str4.lstrip())
print(str4.rstrip())

