# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

###########################################
# FOR LOOP
###########################################

people = ['John', 'Will', 'janet']

# for loop
# =========
for person in people:
    print('Current Person: ', person)
# Current Person:  John
# Current Person:  Will
# Current Person:  janel

# Break out of loop
# ==================
for prsn in people:
    print('Person: ', prsn)
    if prsn == 'Will':
        break
# Person:  John
# Person:  Will

for persn in people:
    if persn == 'Will':
        break
    print('person: ', persn)
# person:  John

# Continue
# =========
for individual in people:
    if individual == 'Will':
        continue
    print('Individual: ', individual)
# Will was skipped
# output
# Individual:  John
# Individual:  janet

# Range
# =======
for i in range(len(people)):
    print('Ranged ppl ', people[i])
# Ranged ppl  John
# Ranged ppl  Will
# Ranged ppl  janet

# Range Numbers
# ==============
for i in range(0, 10):
    print('Number ', i)
# Number  0
# Number  1
# Number  2
# Number  3
# Number  4
# Number  5
# Number  6
# Number  7
# Number  8
# Number  9

###########################################
# WHILE LOOP
###########################################

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print('Counter: ', count)
    count += 1
# Counter:  0
# Counter:  1
# Counter:  2
# Counter:  3
# Counter:  4
# Counter:  5
# Counter:  6
# Counter:  7
# Counter:  8
# Counter:  9
# Counter:  10
