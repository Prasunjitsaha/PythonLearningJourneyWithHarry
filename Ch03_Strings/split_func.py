a="Hello Prasunjit! Welcome to Python Programming World"
b="Harry!How are You?"
print(a.split())  # Splits the string into a list of words
print(a.split(" ")) # Splits the string using space as the delimiter
print(a.split(" ", 2))  # Splits the string into a maximum of 3 parts
print(a.split(" ", 1))  # Splits the string into a maximum of 2 parts
print(a.split("P"))  # Splits the string using "P" as the delimiter
print(a.split("P", 1))  # Splits the string into a maximum of 2 parts using "P" as the delimiter
print(a.split("P", 2))  # Splits the string into a maximum of 3 parts using "P" as the delimiter
print(a.split("P", 3))  # Splits the string into a maximum of 4 parts using "P" as the delimiter
print(a.split("P", 4))  # Splits the string into a maximum of 5 parts using "P" as the delimiter
print(b.split("r"))