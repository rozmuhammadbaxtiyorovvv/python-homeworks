# 1. capitalize()
# Makes the first character uppercase
text = 'hello world'
print(text.capitalize())

# 2. casefold()
# Converts the entire string to lowercase (stronger than lower()).
text = "HELLO"
print(text.casefold())

# 3. center()
# Centers the string within a specified width.
text = "Python"
print(text.center(20, "$"))

# 4. count()
# Counts how many times a value appears.
text = "assalomu aleykum yaxshimisiz ishlaringiz yaxshimi ahvollaringz nichik "
print(text.count("a"))

#  5. encode()
# Converts a string into bytes.
text = "Nichiksan Jura"
print(text.encode())


# 6. endswith()
# Checks if the string ends with a specific value.
text = "thisfileendswith.pdf"
print(text.endswith(".pdf"))

# 8. find()
# Returns the position of the first occurrence.
text = "Python is easy to learn"
print(text.find("Python"))

# 9. format()
# Inserts values into placeholders.
text = "Wassup {}, how are you?"
print(text.format("Rozmuhammad"))

# 11. index()
# Like find(), but gives an error if not found.
text = "Hello Python"
print(text.index("Python"))

# 12. isalnum()
# Checks if all characters are letters or numbers.
text = "Men20yoshdaman"
print(text.isalnum())

# 13. isalpha()
# Checks if all characters are letters.
text = "Menyigirmayoshdaman"
print(text.isalpha())

# 15. isdecimal()
# Checks if all characters are decimal numbers.
text = "123"
print(text.isdecimal())

# 16. isdigit()
# Checks if all characters are digits.
text = "1213"
print(text.isdigit())

# 17. islower()
# Checks if all characters are lowercase.
text = "my name is rozmuhammad"
print(text.islower())

# isupper()
# Checks if all letters are uppercase.
text = "MY NAME IS ROZMUHAMMAD"
print(text.isupper())
print(text.lower())

# istitle()
# Checks if all letters are uppercase.
text = "My Name Is Rozmuhammad"
print(text.istitle())

# split
text = "Python, Php, Javascript, Html, Css"
print(text.split(","))

# replace
text = "my name is rozmuhammad"
print(text.replace("rozmuhammad", "Ali"))
