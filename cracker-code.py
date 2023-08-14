# Import module
import hashlib
# Import wordlist from wordlist.py file
from Wordlist import wordlist


# Create a function to hash and return a string using the sha-256 function
def hash_sha256(hash_password):
    hashed_result = hashlib.sha256(hash_password.encode()).hexdigest()
    return hashed_result


# Declare an empty list to append the hashed wordlist to
hashed_word_list = []

# Go through the wordlist array in 'Wordlist.py' file
# Change every word in the wordlist list to lowercase using the lower method
# Hash each word in wordlists using the SHA256 algorithm and append to the hashed_word_list list
for word in wordlist:
    lower_case_word = word.lower()
    hashed_word_list.append(hash_sha256(lower_case_word))


# Ask the user for their password to crack and change it to lowercase
user_password = input('Enter a password: ').lower()

# Hash the users password with the SHA256 algorithm
user_hashed_password = hash_sha256(user_password)

# Check to see if the users password is in the hashed_word_list list
if user_hashed_password in hashed_word_list:
    print('Your password: {} is easy to crack'.format(user_password))
    print('Try using a password that consists of different words and include symbols and numbers')
else:
    print("That could be a good password as it wasn't in my common passwords wordlist")


