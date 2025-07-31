a="0123456789"
b="abcdefghij"
c="23456789"
print(c[1:6:4])  #6th index is excluded, so it will print 3, 7 after skipping 4 characters
print(a[0:9:2])  #9th index is excluded, so it will print 0, 2, 4, 6, 8
                  # after skipping 2 characters
print(a[0:9:3])  #9th index is excluded, so it will print 0, 3, 6, 9 after skipping 3 characters
print(b[0:9:5])  #9th index is excluded, so it will print a, f after skipping 5 characters                