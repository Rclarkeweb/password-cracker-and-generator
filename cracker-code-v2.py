# Import modules
import hashlib
import urllib.request


# Create functions
# Create a function to use the urllib module to open, read and decode a txt file that contains common passwords
# Use Try and Except to handle errors if the url can't be found
def open_url_file(url):
    try:
        file = urllib.request.urlopen(url).read().decode('UTF-8')
    except Exception as error:
        print("The url could not be found", error)
        exit()
    return file


# Create a function to hash and return a string using the sha-256 function
def hash_sha256(hash_password):
    hashed_result = hashlib.sha256(hash_password.encode()).hexdigest()
    return hashed_result


# Create a bruteforce function
# Use a for loop to go through each password in the password list and change it lowercase
# Check if the users hashed password is equal to the hashed passwords in the list
# If the users password couldn't be found print a string
def brute_force(password_list, users_hashed_password):
    for password in password_list:
        password.lower()
        if hash_sha256(password) == users_hashed_password:
            print('Your password: {} was easy to crack'.format(password))
            print('Try using a password that consists of different words and include symbols and numbers')
            exit()
    print("I couldn't guess your password! This means it's not in my wordlist of common passwords "
          "and it could be a strong password!")
    exit()


# Enter the url of the common wordlist
url = 'https://raw.githubusercontent.com/DavidWittman/wpxmlrpcbrute/master/wordlists/1000-most-common-passwords.txt'

# Ask the user for their password and convert it to lowercase
user_password = input('Enter a password: ').lower()

# Hash the users password
users_hashed_password = hash_sha256(user_password)

# Open and read the url txt file
word_list = open_url_file(url)

# Turn the wordlist into a list of common passwords
password_list = word_list.split('\n')

# Run / Execute the brute force function
brute_force(password_list, users_hashed_password)
