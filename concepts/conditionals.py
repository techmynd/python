# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 6

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# IF
# ===
# print('IF CONDITION >>')
if x == y:
    print(f'{x} is equal to {y}')

# IF/ELSE
# ========
# print('IF ELSE CONDITION >>')
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is less than {y}')

# elif
# =====
# print('IF ELSE/IF ELSE ELSE CONDITION >>')
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than {y}')

# Nested Condition
# =================

if x > 2:
    print()
    if x > y:
        print()
    else:
        print()
elif x < 2:
    print()
else:
    print()


# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x > 2 and x <= 10:
    print()

# 0r
if x > 2 or x <= 10:
    print()

# not
if not(x == y):
    print()

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

# in
m = 4
numbers = [1, 2, 3, 4, 5]  # list / arrays
if m in numbers:  # True or False / Bool output
    print(m in numbers)
# True

# in
v = 41
numberss = [1, 2, 3, 4, 5]  # list / arrays
if v not in numberss:  # True or False / Bool output
    print(v in numberss)
# False

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
j = 1
k = 3
if j is k:
    print(j is k)
# False

# is not
if x is not y:
    print(x is y)
