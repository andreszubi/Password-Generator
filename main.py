import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator, a tool to generate random passwords for your accounts.")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))


#Create variables to store the passwords
password = ""
password2 = ""

#Generate the passwords using for loops, random.choice() to select a random letter, symbol, or number from the lists.
for i in range(num_letters):
    password += random.choice(letters)
    password2 += random.choice(letters)

for i in range(num_symbols):
    password += random.choice(symbols)
    password2 += random.choice(symbols)
for i in range(num_numbers):
    password += random.choice(numbers)
    password2 += random.choice(numbers)

#Sort the passwords by type and character
password = sorted(password, key=lambda c: (0 if c.isalpha() else 2 if c.isdigit() else 1, c))
password2 = sorted(password2, key=lambda c: (0 if c.isalpha() else 2 if c.isdigit() else 1, c))

#Test print the passwords
print(password)
print(password2)

#Join the passwords into strings
password = "".join(password)
password2 = "".join(password2)

#Choose a random password from the two passwords
final_password = random.choice([password, password2])

#Print the final password
print(f"Your password is: {final_password}")
print("Thank you for using the PyPassword Generator!")

#Ask the user if they want to generate another password
another_password = input("Do you want to generate another password? (y/n)\n")
if another_password == "y":
    main()
else:
    print("Thank you for using the PyPassword Generator!")



