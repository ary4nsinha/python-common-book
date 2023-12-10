# block of code that will execute if the condition is true 
age = int(input('How old are you?: '))

if age >= 18:
    print("You're practically in your grave homie")
    
elif age < 110:
    print("You are an adult!")
    #it will print you are an adult even if you put 400 age 
elif age < 0:
    print("You haven't been born yet dawg")

else: 
    print("You are a minor :(")

#order of your if statements matters 