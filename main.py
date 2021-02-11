# Notes: you can generate passowrd using string. ex: aa*()12
# but if you want to generate a password like *a(a2)1, you need to shuffle the string. 

# Random has a method called: random.shuffle(list)
# this function only works with list.append

# So, the best way to solve this challenge is first add all the letters, symbols and numbers into a list. shuffle it, and then traverse through the list to convert a string from list.

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# rand_letter = ""
# for char in range(1, nr_letters + 1):
#   rand_letter = rand_letter + random.choice(letters)
# #print(rand_letter)

# rand_symbol = ""
# for sym in range(1, nr_symbols + 1):
#   rand_symbol = rand_symbol + random.choice(symbols)
# #print(rand_symbol)

# rand_num = ""
# for num in range(0, nr_numbers):
#   rand_num = rand_num + random.choice(numbers)
# #print(rand_num)

# password = (rand_letter + rand_symbol + rand_num)
# #rand_password = random.sample(password)
# print(password)

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
#print(password_list)

for sym in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))
#print(password_list)

for num in range(1, nr_numbers+1):
  password_list.append(random.choice(numbers))
#print(password_list)
random.shuffle(password_list)
#print(password_list)

pass_str = ""

for i in password_list:
  pass_str = pass_str + i
print(pass_str)


  
