# Task # 1:
# Write a program to take input a number and disply its multiplication table.

# n = int(input("Enter any number: "))
# for i in range(1,11) :
#     r = n * i
#     print(n," x ", i , "=", r)

# Task # 2:
# Write a program to take input names of 10 friends and make a list of friend names using for loop.
friends = []
# for i in range(1, 11) :
#     z = input("Enter your friends name: ")
#     friends.append(z)
# print(friends)

# Task # 3:
# write a program to add two integer lists using for loop and make another list using append function.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = []
# for i in range(len(list1)):
#     result.append(list1[i] + list2[i])
# print(result)

# Task # 4:
# write a program to print the sum of a list elements.
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total += num
# print(total)

# Task # 5:
#Write a program print the even and odd numbers lesser than  100.
# odd = range(1, 100, 2)
# print("ODD NUMBERS:")
# for n in odd:
#     print(n)
# even = range(2, 100, 2)
# print("EVEN NUMBERS:")
# for n in even:
#     print(n)

# Task # 6:
# Write a program to display convert the list of string numbers into list of integers
string_numbers = ["10", "20", "30", "40", "50"]
integer_numbers = []
for string_num in string_numbers:
    integer_num = int(string_num)
    integer_numbers.append(integer_num)
print("List of integer numbers: ", integer_numbers)