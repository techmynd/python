# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# These are OBJECTS in Python

# person dictionary or object
# ===========================
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
print(person)
# {'first_name': 'John', 'last_name': 'Doe', 'age': 30}

#/////////////////#
# constructor//////
#/////////////////#

person_c = dict(
    first_name='Jon',
    last_name='D',
    age=20
)
print(person_c)
# {'first_name': 'Jon', 'last_name': 'D', 'age': 20}

# Access value
# ============
print(person['first_name'])  # John
# or
print(person.get('last_name'))  # Doe

# Add key/value
# =============
print(person)
# {'first_name': 'John', 'last_name': 'Doe', 'age': 30}
person['phone'] = '111-222-333-444'
print(person)
# {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'phone': '111-222-333-444'}

# Get Keys
# ========
print(person.keys())
# dict_keys(['first_name', 'last_name', 'age', 'phone'])

# Get Values
# ==========
print(person.items())
# dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 30), ('phone', '111-222-333-444')])

# Make Copy
# ==========
person2 = person.copy()
person2['city'] = 'Lahore'
print(person2)
# {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'phone': '111-222-333-444', 'city': 'Lahore'}

# Remove item
# ============
print(person)
# {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'phone': '111-222-333-444'}
del(person['age'])
# or
person.pop('phone')
print(person)
# {'first_name': 'John', 'last_name': 'Doe'}

# Length
# =======
print(person)
# {'first_name': 'John', 'last_name': 'Doe'}
print(len(person))
# 2

# List of Dict
# =============
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'John', 'age': 32}
]
print(people)
# [{'name': 'Martha', 'age': 30}, {'name': 'John', 'age': 32}]
print(people[1]['age'])
# 32


# Clear
# ======
person.clear()
print(person)
# {}

'''
person.update()
person.get()
'''
