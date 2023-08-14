# Password Generator
import random
import string

# Generate list of letters, numbers and symbols from string module
letters_lc = string.ascii_lowercase
letters_lc_list = [*letters_lc]

letters_uc = string.ascii_uppercase
letters_uc_list = [*letters_uc]

letters = letters_lc_list + letters_uc_list

numbers = string.digits
numbers_list = [*numbers]

symbols = string.punctuation
symbols_list = [*symbols]

# Ask user for input
print('Lets generate a secure password for you!\n')

# Ask for number of letters, numbers and symbols in password
pw_letters = int(input('How many letters do you want? \n'))
pw_numbers = int(input('How many numbers do you want? \n'))
pw_symbols = int(input('How many symbols do you want? \n'))

# Randomise lists
random.shuffle(letters)
random.shuffle(numbers_list)
random.shuffle(symbols_list)

# Create empty string variable to store password in
password = ''

# Loop through each list and add the number of letters/numbers/symbols to the password variable
for lc in range(1, pw_letters + 1):
    random_letters = random.choice(letters)
    password += random_letters

for number in range(1, pw_numbers + 1):
    random_numbers = random.choice(numbers_list)
    password += random_numbers

for symbol in range(1, pw_symbols + 1):
    random_symbols = random.choice(symbols_list)
    password += random_symbols

# Store the generated in new variable
random_password = [*password]

# Shuffle/randomise the password
random.shuffle(random_password)

# Display it as a string
user_password = ''.join(random_password)

# Display the random generated password to the user
print(f"You're generated password is: {user_password}")