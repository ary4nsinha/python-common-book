#type-casting is the ability to convert a datatype to another datatype 

x =1 #int 
y = 2.0 #float
z = "3" #str 


print(x)
print (int(y)) #will print it as integer/ this is not permanent chagne 

print(z)

y = int(y) #perma 
print(y)

print(z*3) #wont work need to type cast 

z = int(z) #this works 
print(z*3)

#converting to floating point number 
x = float(x)
y = float(y)
z = float(z)
print(x)
print(y)
print(z*3)
