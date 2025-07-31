a="hello!!!"
print(a.endswith("!!!"))  # Checks if the string ends with "!!!"
print(a.endswith("hello"))  # Checks if the string ends with "hello"
b="welcome to python"
print(b.endswith("to",4,10))  # Checks if the substring "to" is at the end of the string from index 4 to 10
print(b.endswith("to", 0, 7))  # Checks if the substring "to" is at the end of the string from index 0 to 7
print(b.endswith("python", 11, 17))# True  # Checks if the substring "python" is at the end of the string from index 11 to 17
print(b.endswith("python", 11, 16))# False   # Checks if the substring "python" is at the end of the string from index 11 to 17