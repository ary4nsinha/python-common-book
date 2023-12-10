with open("example.txt", 'w') as file:
    file.write("Hello, this is a sample file created using Python!")

print("File created successfully in the current directory.")

with open("example.txt", 'a') as file:
    file.write("\nMy name is aryan")

with open("example.txt", 'a') as file:
    a = "\nHow are you?\nWhat are your plans for tommorow?\nSounds Good!\n I am going to Himalayas\n Ok bye \n Great enjoy your trip balle balle"
    file.writelines(a)

with open("example.txt",'r') as file:
    print(file.read())

with open("example.txt",'r') as file:
    print(file.read(5))

with open("example.txt",'r') as file:
    for x in range(0,2):
        print(file.readline())

with open("example.txt",'r') as file:
    print(file.seek(50,0))
    print(file.tell())
    
