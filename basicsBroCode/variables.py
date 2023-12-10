# a variable is a container for a value

name = "aryan"
print("hello" +name) #concatinating strings

age = 20 #check the data-type of variable on the console
print(type(age))

last_name = "sinha" #you can add two variables as long as they are of the same data-type
full_name = name + " " + last_name
print("Hello" + " " + full_name)

#int data-type 
my_age = 45
my_age = my_age + 1
print(my_age)

#another way to do this 
my_age += 1
print(my_age)

#print("Your age is:"+age) this will show an error as you cant concatinate diff variables
#to make it work
print("Your age is:" +str(age))
#you just need to add a string cast , this is an example of type casting


#float = decimal portion can be stored 
height = 250.5 
print(height)
print(type(height))

print("Your height is:" +str(height) + "cm")

#boolean data-type stores true or false 
human = True
print(human)
print(type(human))
print("Are you a human? "+ str(human))