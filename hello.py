import sys

# Respond here: The end statement appends a string at the end of the print
#               statement, overriding the default endline.

print("Hello, ", end = '')
print(sys.argv[1], end=', ')
print(sys.argv[2], end=' and ')
print(sys.argv[3], end='')
print("! Welcome.")

# To run this code: python hello.py Meghan Ned Francie
