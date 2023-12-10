# tuple = collection which is ordered and unchangeable used to group together related data 
student = ("aryan",20,"male")

print(student.count("aryan"))
print(student.index("male"))

for x in student:
    print(x)

if "aryan" in student:
    print("aryan is here ")