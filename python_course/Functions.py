Write a function to reverse a given string
def reverse_string(input_string):
    reversed_string=input_string[::-1]
    return reversed_string
#Calling Syntax
original_string="Check"
result=reverse_string(original_string)
print(result)

# Implement a function that counts the number of vowels in a string.
def vowels(string):
    vowels = ("aeiouAEIOU")
    count = 0
    for vowel in string:
        if vowel in vowels:
            count += 1
    return count
#Calling syntax
string = "aeiou"
result = vowels(string)
print(f"Number of vowels in the string: {result}")

# Create a function that finds the maximum and minimum values in a list.
def max_min(list):
    max= list[0]
    min= list[0]
    for n in list:
        if n>max:
            max=n
        elif n<min:
            min=n
    return max,min
# Calling Syntax
numbers = [5,6,2,3,4,7]
max, min= max_min(numbers)
print(f"Maximum value: {max}")
print(f"Minimum value: {min}")

Write a function to calculate the sum and average of elements in a list.
def cal_average(list):
    total = 0
    count = 0
    for num in list:
        total += num
        count += 1
    average_number = total/count
    return  average_number
# Calling Syntax
numbers = [8,9,6,2,4]
average = cal_average(numbers)
print(f"Average of numbers: {average}")

# Implement a function to calculate the factorial of a given number.
def cal_factorial(number):
    r= 1
    for i in range(1, number + 1):
        r *= i
    return r
# CAlling Syntax:
number = 5
factorial = cal_factorial(number)
print(f"The factorial of {number} is: {factorial}")

# Write a function to check if a given string is a palindrome.
def check_palindrome(string):
    return string == string[::-1]
# Calling Syntax:
input = "civic"
result = check_palindrome(input)
if result == False:
    x="is not"
else:
    x ="is"
print(f"The given string {x} a palindrome")

#Implement a calculator function that takes operator and operands as input and performs the corresponding operation.
def calculator(operator, o1, o2):
    if operator == '+':
        r=o1 + o2
    elif operator == '-':
        r=o1 - o2
    elif operator == '*':
        r=o1 * o2
    elif operator == '/':
        r = o1 / o2
    else:
        return "Invalid Operand"
    return r
# Calling Syntax:
operator_input = input("Enter operator (+, -, *, /): ")
o1_input = float(input("Enter the first operand: "))
o2_input = float(input("Enter the second operand: "))

result=calculator(operator_input, o1_input, o2_input)
print(f"Result: {result}")

# Create a function to check if a number is prime
def prime(number):
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is a composite number")
            return
    print(f"{number} is a prime number")
    return
# Calling Syntax
number = 15
prime(number)
