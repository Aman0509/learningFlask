"""
User Authentication

- So far anyone has been able to access any page of our web applications.
- However, often, you’ll want to restrict access to only registered users.

- We’ll discuss
    - Password Hashing
    - Flask-Login Library
    - Flask OAuth

Password Hashing

- When your website has User Authentication, you will need to store their usernames and passwords.
- For security purposes, we will never want to store the raw text of the password.
- We can use a hash function to help with this.
- A hash function is an algorithm that can take in a document (password) and return back a secure hash digest.
- It is secure because given the hash, a person can not determine what the original password was.
- For example, let’s imagine a very simple (and insecure) hash function.
    - Our example hash function will count the number of letters in a password: mypassword → 10
    - We would save the hash (10).
    - Now given the number 10, you would not be able to determine what the original password was.
- There are already cryptographically secure hashing algorithms and libraries for us to use (you should never write your own)!
- Then when the user provides a password, we can simply check it against its hashed form for a match with our saved hash.
- There are two useful libraries for this:
    Bcrypt
    Werkzeug
"""

from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

password = "mysecretpassword"

# Create a Bcrypt object
bcrypt = Bcrypt()

print("Bcrypt Hashing Library".center(50, "="))

# Hash the password
hashed_password = bcrypt.generate_password_hash(password=password)
print("bcrypt_pass_hash - ", hashed_password)

# Comparing the password comming from the user with the hashed password
# If the password is correct, it will return True
print("bcrypt_pass_hash_compare_with_correct_password - ",bcrypt.check_password_hash(hashed_password, password))
print("bcrypt_pass_hash_compare_with_wrong_password - ", bcrypt.check_password_hash(hashed_password, "someotherpassword"))

print()
print("Werkzeug Hashing Library".center(50, "="))

# Using werkzeug library
# Generate a hash
werk_hashed_password = generate_password_hash(password=password)
print("werk_pass_hash - ", werk_hashed_password)

# Compare the password with the hash
print("werk_pass_hash_compare_with_correct_password - ", check_password_hash(werk_hashed_password, password))
print("werk_pass_hash_compare_with_wrong_password - ", check_password_hash(werk_hashed_password, "someotherpassword"))

print()