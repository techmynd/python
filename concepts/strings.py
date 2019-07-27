# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Javed'  # str
age = 37        # int

#######################################
# Concatinate
#######################################

print('Hello ' + name)
# can only concatinate strings, not int
# convert int into string and then concatinate
print('STRING WITH INT CONCAT>>> ' + 'Hello ' +
      name + ' and I am ' + str(age) + ' years old')

#######################################
# String Formatting
#######################################

# Arguments by position
print('REGULAR ORDER>>> ' + '{},{},{}'.format('a', 'b', 'c'))
# change order
print('CHANGE ORDER>>> ' + '{2},{0},{1}'.format('a', 'b', 'c'))

# Arguments by name
print('My name is {myName} and I am {myAge} years old'.format(
    myName='Javed', myAge='37'))
# or
name = 'Javed Khalil'  # str
age = 32               # int
print('My name is {myName} and I am {myAge} years old'.format(
    myName=name, myAge=age))

#######################################
# F-Strings (only in python 3.6+)
#######################################
print('F-Strings >>> ' + f'My name is {name} and I am {age} years old')

#######################################
# String Methods // Methods are functions so these will need to be invoked like
# method(), function(), something(), print(methodname())
#######################################
s = 'hElLo wOrLd wworld'

# capitalize first letter / uppercase / lowercase / swap case
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())

# Get Length
print('Length of Characters in a Variable including empty spaces >>> ', len(s))

# Replace
# Replace something in string // case sensitive
print('REPLACING WORLD WITH EVERYONE >>> ' + s.replace('wOrLd', 'everyone'))
# Chaining // first convert to lowercase and then replace it with anothing else
print(s.lower().replace('world', 'everyone else'))

print('@@@@@@@@@@@@@@@@@')

# Count
thingToCount = 'w'
print('THERE ARE >> ' + str(s.count(thingToCount)) + ' << w IN -> ' + s)

# Starts With
print('STARTS WITH >> ', str(s.startswith('hElLo')))

# Ends With
print('ENDS WITH >> ', s.endswith('d'))

# Split into a List of words
print('SPLIT WORDS >> ', s.split())

# Find Position
print('FIND E POSITION >> ', s.find('E'))

# is all alphanumeric // letters and numerals // either a letter (a, b, c) or a number (1, 2, 3) // no spaces
print(s.isalnum())

# is all alphabetic // letters // a, b, c, d, e, f, g, h ... // no spaces
print(s.isalpha())

# is all numeric // numbers // 1,2,3 // no spaces
print(s.isnumeric())

print('@@@@@@@@@@@@@@@@@')

# s is a variable, right, type s in IDE and dropdown list will show you available methods

# more methods
'''
s.index()
s.casefold()
s.find()
s.format_map()
s.index()
s.encode()
s.expandtabs()
s.isascii()
s.isdecimal()
s.isdigit()
s.isspace()
s.strip()
s.join()
'''
