# # first test assignment using and understanding print function
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
#
# # printing hello would and duplicating it using \n
print("Hello World! \n Hello World!")
#
# using the print and input function and string concatenation
print("Hello " + input("What is your name?"))

#switching variables
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

#Building a Band Name generator using location and pet name.
#welcome message
print("Welcome to Band Name Generator")
#Location where user grew up
location = input("Where did you grow up? \n")
#childhood name for pet
pet_name = input("What was the name of your childhood pet? \n")
#Band Name Generated
print("Your band name is: \n" + location + " " + pet_name)