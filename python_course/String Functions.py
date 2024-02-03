word_list = ["apple", "banana", "cherry", "date"]
# Create a list of words.
print("List:", word_list)

# Create a string from the list.
_string = ' '.join(word_list)
print("String:", _string)

# Capitalize the first letter of the entire string. Print the modified string.
modified_string = _string.capitalize()
print("Capitalize the first letter:", modified_string)

# Find and print the index of the first occurrence of the letter 'a' in the string.
index_ = _string.find('a')
print("The letter 'a' occurs at index", index_, "first time")

# Count and print the number of occurrences of the letter 'a'.
count_of_a = _string.count('a')
print("The letter 'a' occurs", count_of_a, "times in", _string)

# Replace 'a' with 'x'. Print the modified string.
modified_string = _string.replace('a', 'x')
print("Replaced 'a' with 'x':", modified_string)

# Remove leading and trailing whitespaces. Print the modified string.
_input = " " + _string + " "
modified_string = _input.strip()
print("Remove leading and trailing whitespaces:", modified_string)

# Split the string back into a list. Print the resulting list.
resulting_list = _string.split()
print("Resulting list:", resulting_list)
