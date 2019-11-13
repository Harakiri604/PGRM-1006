import pandas as pd

users = pd.read_csv("users.txt")
print(users.head(10))

print(len(users))
print(users['password'].nunique())

#Create a column and populate with password length
users['length'] = users.password.apply(len)
print(users.head(10))

#Let's flag all with <8
users['too_short'] = users.length < 8
print(users.head(10))

#Import the passwords file
common_passwords = pd.read_csv("10-million-password-list-top-1000000.txt", header=None)
print(common_passwords.head(20))

#Create a true/false column for those where passwords are common
users['common_password'] = users.password.isin(common_passwords[0])
print(users.head(10))

#How many users have common passwords
print("Users with common passwords: ", end="")
print(users.common_password.sum())

#Import the dictionary
words = pd.read_csv("google-10000-english.txt", header=None)
print(words.head(10))

#Same as with common passwords
users['common_word'] = users.password.isin(words[0])
print(users.head(10))

print("Users with passwords as common words: ", end="")
print(users.common_word.sum())

#Failed both tests
users['you_are_bad'] = users.too_short | users.common_password | users.common_word
print(users.head(10))

print("Users who are shit: ", end="")
print(users.you_are_bad.sum())