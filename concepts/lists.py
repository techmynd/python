# A List is a collection which is ordered and changeable. Allows duplicate members.

# lists are array

# Create List
numbers = [1, 2, 3, 4, 5]
print(type(numbers))
print(numbers)

# Create List Using Constructor
NumbersList = list((1, 2, 3, 4))
print(NumbersList)

print('@@@@@@@@@@@@@')

fruits = ['apples', 'oranges', 'grapes', 12]
print(fruits)
print(fruits[1])
print(fruits[3])
# get length
print('NUMBER OF ITEMS >> ', len(fruits))

print('@@@@@@@@@@@@@')

# Append to List
fruits.append('Mangos')
print('Mangos ADDED >> ', fruits)

# remove
fruits.remove('oranges')
print('oranges REMOVED >> ', fruits)

# insert at specific position
fruits.insert(2, 'Peach')
print('Peach INSERTED AT POSITION 2 >> ', fruits)

# remove from certain position
fruits.pop(1)
print('grapes AT FIRST POSITION REMOVED >> ', fruits)

# reverse array
fruits.reverse()
print('ORDER REVERSED >> ', fruits)

# sort list
fruit = ['mangos', 'apples', 'Cherry', 'oranges', 'grapes']
fruit.sort()
print('ORDER ALPHABATICALLY SORTED >> ', fruit)

# reverse sort list
fruit.sort(reverse=True)
print('REVERSE SORTED >> ', fruit)

# more list methods // array methods
fruits.clear()
fruits.copy()
fruits.count(2)   # takes one argument
# fruit.extend()  # int object not iterable // takes one argument
# fruits.index()
