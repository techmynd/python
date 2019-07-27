# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

'''
print('hello py')
'''

# no semicolons, no curly brackets

# Declare Variables
x = 1                     # int or whole number
y = 2.5                   # float / decimal number
name = "Javed"            # string
Name = 'Javed Khalil'     # string
is_cool = True            # bool (bool is technical term not boolean)
is_Bad = False            # bool
isCool = True             # bool

# Multiple Assignment
x, y, name, is_cool = (1, 2.5, 'Javed', True)

print(isCool)               # print

# multiple print
print(x, y, name, is_cool)  # print

# basic math
a = x+y
print(a)

# check type
print(type(is_cool))

# casting
m = str(x)
n = int(y)
# n = float(x)
print("change type of x int to str", type(m))  # we converted int into string
