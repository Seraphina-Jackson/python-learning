# numbers = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
# for number in numbers:
#     max = number
# print(max)

#Gauss Challenge
#print the sum of the numbers (1 - 100)
# sum = 0
# for number in range(1,101):
#     sum += number
# print(sum)

#FizzBuzz
# for number in range(1,101):
#     if number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(number)
    
#day project
#Password Generator
import random

numbers = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters = "!@#$%^&*()_+-="

print("Welcome to the PyPassword Generator!")

overall = int(input("How many characters would you like in your password? : "))

pool = ""

user_characters = input("Include characters? (y/n) : ")
user_numbers = input("Include Numbers? (y/n) : ")
user_letters = input("Include letters? (y/n) : ")

if user_characters == "Y" or user_characters == "y":
    pool = pool + characters

if user_numbers == "Y" or user_numbers == "y":
    pool = pool + numbers

if user_letters == "Y" or user_letters == "y":
    pool = pool + letters
if pool == "":
    print("Error: You must choose at least one option!")
else:
    password = ""

    for i in range(overall):
        random_char = random.choice(pool)
        password = password + random_char

    print("Your new password is: " + password)
    
    





