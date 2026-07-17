text = "Assalomu Aleykum Dear Guests And My Name Is Rozmuhammad And Im 20 Years Old"
text2 = "I Was Born In 2006 And I Like To Code"
# capitalize()	Converts the first character to upper case
print(text.capitalize())
# casefold()	Converts string into lower case
print(text.casefold())
# center()	Returns a centered string
print(text.center(100, "*"))
# count()	Returns the number of times a specified value occurs in a string
print(f"Berilgan matnda umumiy 'a' harfi {text.count('a')} marta qatnashgan")
# encode()	Returns an encoded version of the string
print(text.encode())
# endswith()	Returns true if the string ends with the specified value
print(text.endswith("old"))
# expandtabs()	Sets the tab size of the string
print(text.expandtabs())
# find()	Searches the string for a specified value and returns the position of where it was found
print(text.find("a"))
# format()	Formats specified values in a string
print(text.format("a", "b", "c"))
# format_map()	Formats specified values in a string
print(text.format_map({"a": "a", "b": "b", "c": "c"}))
# index()	Searches the string for a specified value and returns the position of where it was found
print(text.index("a", 10))
# isalnum()	Returns True if all characters in the string are alphanumeric
print(text.isalnum())
# isalpha()	Returns True if all characters in the string are in the alphabet
print(text.isalpha())
# isascii()	Returns True if all characters in the string are ascii characters
print(text.isascii())
# isdecimal()	Returns True if all characters in the string are decimals
print(text.isdecimal())
# isdigit()	Returns True if all characters in the string are digits
print(text.isdigit())
# isidentifier()	Returns True if the string is an identifier
print(text.isidentifier())
# islower()	Returns True if all characters in the string are lower case
print(text.islower())
# isnumeric()	Returns True if all characters in the string are numeric
print(text.isnumeric())
# isprintable()	Returns True if all characters in the string are printable
print(text.isprintable())
# isspace()	Returns True if all characters in the string are whitespaces
print(text.isspace())
# istitle()	Returns True if the string follows the rules of a title
print(text.istitle())
# isupper()	Returns True if all characters in the string are upper case
print(text.isupper())
# join()	Joins the elements of an iterable to the end of the string
print(text.join(text2))
# ljust()	Returns a left justified version of the string
print(text.ljust(100, "*"))
# lower()	Converts a string into lower case
print(text.lower())
# lstrip()	Returns a left trim version of the string
print(text.lstrip())

# maketrans()	Returns a translation table to be used in translations
# print(text.maketrans())
# partition()	Returns a tuple where the string is parted into three parts
print(text.partition("a"))
# replace()	Returns a string where a specified value is replaced with a specified value
print(text.replace("a", "b"))
# rfind()	Searches the string for a specified value and returns the last position of where it was found
print(text.rfind("a"))
# rindex()	Searches the string for a specified value and returns the last position of where it was found
print(text.rindex("a"))
# rjust()	Returns a right justified version of the string
print(text.rjust(100, "*"))
# rpartition()	Returns a tuple where the string is parted into three parts
print(text.rpartition("a"))     
# rsplit()	Splits the string at the specified separator, and returns a list
print(text.rsplit("a"))
# rstrip()	Returns a right trim version of the string
print(text.rstrip())
# split()	Splits the string at the specified separator, and returns a list
print(text.split("a"))
# splitlines()	Splits the string at line breaks and returns a list
print(text.splitlines())

# startswith()	Returns true if the string starts with the specified value
print(text.startswith("a"))
# strip()	Returns a trimmed version of the string
print(text.strip())
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
print(text.swapcase())
# title()	Converts the first character of each word to upper case
print(text.title())
# upper()	Converts a string into upper case
print(text.upper())