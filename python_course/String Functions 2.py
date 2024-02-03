input_string = "My country is Pakistan"

# Create a list of words.
word_list = input_string.split()
print("List:", word_list)

# Create a string from the list.
_list = ["My Country is Pakistan"]
_string = ' '.join(_list)
print("String:", _string)

# Capitalize the first letter of the entire string. Print the modified string.
modified_string = input_string.capitalize()
print("Capitalize the first letter:", modified_string)

# Find and print the index of the first occurrence of the letter 'a' in the string.
_input = input_string
index_ = _input.find('a')
print("The letter 'a' occurs at index", index_, "first time")

# Count and print the number of occurrences of the letter 'a'.
_input = input_string
count_of_a = _input.count('a')
print("The letter 'a' occurs", count_of_a, "times in", _input)

# Replace 'a' with 'x'. Print the modified string.
_input = input_string
_string = _input.replace('a', 'x')
print("Replaced 'a' with 'x':", _string)

# Remove leading and trailing whitespaces. Print the modified string.
_input = " " + input_string + " "
_string = _input.strip()
print("Remove leading and trailing whitespaces:", _string)

# Split the string back into a list. Print the resulting list.
user_input = input_string
resulting_list = user_input.split()
print("Resulting list:", resulting_list)
