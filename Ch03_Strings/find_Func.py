a="hello world"
print(a.find("world"))  # Finds the index of the first occurrence of "world" in the string
print(a.find("World"))
print(a.find("Python")) # Returns -1 since "Python" is not found in the string      
print(a.find("o", 5))   # Finds the index of the first occurrence of "o" after index 5
print(a.find("o", 0, 5)) # Finds the index of the first occurrence of "o" in the substring from index 0 to 5
print(a.find("o", 0, 10)) # Finds the index of the first occurrence of "o" in the substring from index 0 to 10