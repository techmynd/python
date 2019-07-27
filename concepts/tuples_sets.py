# tuples and sets are also lists and arrays

# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# simple tuple
fruit_tuple = ('Apple', 'Banana', 'Orange', 'Mango')
print(fruit_tuple)

# tuple constructor
c_tuple = tuple(('Apple', 'Banana', 'Orange', 'Mango'))
print(c_tuple)

# get single value
print(fruit_tuple[1])

# tuple object is uncahngable and does not allow object re-assignment
# you can not do like >> fruit_tuple[1] = 'Grapes'

print(len(fruit_tuple))

# delete tuple
'''
del fruit_tuple
print(fruit_tuple)
'''

# more methods
'''
fruit_tuple.count()
fruit_tuple.index()
'''

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@')
# SETS // no duplicates
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@')
# A Set is a collection which is unordered and unindexed. No duplicate members.

print('// SETS //')
fruits_set = {'Apple', 'Orange', 'Mango'}
print(fruits_set)

# no duplicates
fruits_set = {'Apple', 'Orange', 'Mango', 'Mango'}
print('// NO DUPLICATES //')
print(fruits_set)

# check if something is in set
print('// CHECK IF SOMETHING IS IN SET //')
print('Apple' in fruits_set)  # True

# add to set
print('// ADD IN SET //')
fruits_set.add('Grapes')
print(fruits_set)

# remove from set
print('// REMOVE FROM SET //')
fruits_set.remove('Grapes')
print(fruits_set)

# clear set // but dont delete
'''
fruits_set.clear()
'''
# delete set
'''
del fruits_set
'''


# more set methods
'''
fruits_set.add()
fruits_set.clear()
fruits_set.copy()
fruits_set.difference()
fruits_set.difference_update()
fruits_set.discard()
fruits_set.pop()
fruits_set.remove()
fruits_set.union()
fruits_set.update()
'''
