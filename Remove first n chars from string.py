# Remove the first n characters from the string
String = input("Enter a string: ")

# Accept the number of characters to remove
n = int(input("Enter the number of characters to remove: "))

# Remove the first n characters
modified_string = String[n:]

# Print the modified string
print("Modified string:", modified_string)
