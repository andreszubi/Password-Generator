import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator, a tool to generate random passwords for your accounts.")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))

password = ""
password2 = ""

for i in range(num_letters):
    password += random.choice(letters)
    password2 += random.choice(letters)

for i in range(num_symbols):
    password += random.choice(symbols)
    password2 += random.choice(symbols)
for i in range(num_numbers):
    password += random.choice(numbers)
    password2 += random.choice(numbers)

password = sorted(password, key=lambda c: (0 if c.isalpha() else 2 if c.isdigit() else 1, c))
password2 = sorted(password2, key=lambda c: (0 if c.isalpha() else 2 if c.isdigit() else 1, c))


print(password)
print(password2)



# final_password = password + password2

# print(f"Your password is: {final_password}")

