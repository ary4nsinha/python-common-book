#allows us to assign multiple variables at the same time in one line of code 

#inefficient way
#name = "aryan"
#age = 21 
#attractive = True
#print(name )
#print(age )
#print(attractive)
#uses only one line of code 
name, age, attractive = "aryan", 21, True
print(name )
print(age )
print(attractive)

#example 
SpongeBob = 30
Patrick = 30
Sandy = 30
Squidward = 30
# ^ instead of that use this 
SpongeBob = Squidward = Sandy = Patrick = 30
print(SpongeBob)
print(Patrick)
print(Sandy)
print(Squidward)