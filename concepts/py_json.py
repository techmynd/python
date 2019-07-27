# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

# There is a module called json

import json

# sample json
userJson = '{"name": "John", "Age": 27}'

# parse to dictionary // array

user = json.loads(userJson)
# json.loads is like JSON.parse in JS
print(user)
print(user['name'])

# json.dumps // its dumps dictionary into json

dictToJson = json.dumps(user)
print(dictToJson)
