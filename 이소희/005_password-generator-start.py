#Password Generator Project
import random
# 52개 문자
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# 10개 숫자
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# 9개 특수문자
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

rand_letters = random.sample(range(0, len(letters)),nr_letters)
rand_symbols = random.sample(range(0, len(symbols)),nr_symbols)
rand_numbers = random.sample(range(0, len(numbers)),nr_numbers)

pass_letters = ''
pass_symbols = ''
pass_numbers = ''

for num in rand_letters:
  pass_letters += letters[num]
#print(pass_letters)
for num in rand_symbols:
  pass_symbols += symbols[num]
#print(pass_symbols)
for num in rand_numbers:
  pass_numbers += numbers[num]
#print(pass_numbers)
easy_pw = pass_letters + pass_symbols + pass_numbers
print(f"Easy version: {easy_pw}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


rand_pw_list = list(easy_pw)
random.shuffle(rand_pw_list)
print(f"Hard version: {''.join(rand_pw_list)}")
