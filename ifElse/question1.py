# Check if a number is palindrome or not

number = int(input("Enter a number to check if it is palindrome or not: "))

strNumber = str(number)

reversedNumber = strNumber[::-1]  # Corrected the slicing syntax

if reversedNumber == strNumber:
    print("This number is a palindrome")
else:
    print("This number is not a palindrome")
