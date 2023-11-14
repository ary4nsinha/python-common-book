"""
rows = int(input("Enter number of rows: "))
for i in range(1,rows + 1):
    for j in range(1,i+1):
        print(j, end =" ")
    print(" ")
1
12
123
1234
12345


for i in range(1,6):
    print("*"*i)
*
**
***
****
*****

for i in range(1, 6):
    print(str(i) * i)
1
22
333
4444
55555


age = int(input("Enter your age: "))
if age < 18:
    print("You're a minor ")

elif age <= 18:
    print("You're an adult")

else: 
    print("Bingbong")



name = "python programming"
print(name[0:15:2])

"""
a  = 19.22323
print(int(a))