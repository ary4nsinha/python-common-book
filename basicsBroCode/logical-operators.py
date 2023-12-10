#logicsl operators and & or , not

temp = int(input("What is the temperature outside?: "))
if not(temp>=0 and temp <= 30): #both conditions need to be true 
    print("the temperature is good today")
    print("go outside")

elif not (temp < 0 or temp > 30): #any one condition needs to be true 
    print("Stay inside the temperature is bad today")
 
#not just flips true to false 