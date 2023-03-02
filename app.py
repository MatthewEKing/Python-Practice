# from math import *
#
# BASICS & INPUTS
#
# name = input("Enter Your Name: ")
# age = input("Enter Your Age: ")
#
#
# print("So your name is " + name + ", and you're " + age + " years old?")
# print(character_name.replace("Ma", "Ra"))
#
#
# if name == "Matt" or name == "Matthew":
#     print("You have the same name as the Developer!")
# else:
#     print()
#
##################
#
# LISTS
#
# friends = ["Chris", "Randy", "Chris", "Joann", "Al", "Anna", "Jahel"]
# not_friends = ["RYAN"]
#
# friends2 = friends.copy()
#
# print(friends)
#
###################
#
# TUPLES
#
# names = [("Einar", "Thorfinn"), ("Matt", "Al")]
# print(names[1][0])
#
#
###################
#
# FUNCTIONS

# def say_hi(name, age):
#     print("Hello " + name + ", you are " + str(age) + " years old")
#
# say_hi("Matt", 73)
#
#
# def cube(num):
#     return num * num * num
#
# product = cube(3)
# print(product)
#
#
# is_male = True
# is_tall = True
#
# if is_male and is_tall:
#     print("Is Male and tall")
# elif is_male and not(is_tall):
#     print("Is Male and not tall")
# elif not(is_male) and is_tall:
#     print("Is not male and is tall")
# else:
#     print("is not male and not tall")

#
# def num_max(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(num_max(4,123,45))

################

# DICTIONARIES
#
# monthConversion = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }
#
#
# print(monthConversion.get("IJFISA", "Not a valid key"))
#
##################
#
# LOOPS
#
# i = 1
#
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Finished While Loop")
#
# names = ["Matt", "Al", "Randy"]
#
# for index in range(len(names)):
#     print(names[index])


# def raise_to_power(base_num, power_num):
#     result = 1
#     for index in range(power_num):
#         result = result * base_num
#     print(result)
#
# raise_to_power(3,5)


# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
#
# for row in number_grid:
#     for number in row:
#         print(number)

# TRY / EXCEPT
#
# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)


# EXTERNAL FILES

#temp_file = open("temp", "r")

# for lines in temp_file.readlines():
#     print(lines)

#temp_file.close()

temp_file = open("temp", "w")

temp_file.write("\nadded this line")

temp_file.close()