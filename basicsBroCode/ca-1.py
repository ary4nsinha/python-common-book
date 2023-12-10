for i in range(1,5):
    print(str(i) * i)

rows=5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print('')
#for i in range(1,10,)
    #print("*"*i)
#i = 1
#finding the palindrome of a number 
    

#if else 
#strings 
#string slicing
#for and while 
"""rows=5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print('')




for i in range(1,6):
    print(str(i)*i)

a = "python programming"
print(a[0:7])"""

# Using continue
print("Using 'continue':")
for i in range(1, 6):
    if i == 3:
        continue  # Skip iteration when i is 3
    print("Iteration " + str(i))

# Using pass
print("\nUsing 'pass':")
for i in range(1, 6):
    if i == 3:
        pass  # Do nothing when i is 3
    print("Iteration " + str(i))

# Using break
print("\nUsing 'break':")
for i in range(1, 6):
    if i == 3:
        break  # Exit the loop when i is 3
    print("Iteration " + str(i))

# Using return within a function
def example_function():
    print("\nUsing 'return' within a function:")
    for i in range(1, 6):
        if i == 3:
            return  # Return from the function when i is 3
        print("Iteration " + str(i))

example_function()

print("\nProgram Complete")

