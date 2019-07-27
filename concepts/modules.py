# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core Modules
# ==============

# Date Today
import time  # or # from time import time
import datetime  # or # from datetime import date
today = datetime.date.today()

# or
# from datetime import date
# today = date.today()

print('DATE >> ', today)
# 2019-07-27

timestamp = time.time()
print('TIMESTAMP >> ', timestamp)
# 1564204855.659175

# or
# from time import time
'''
timestampp = time()
print('TIMESTAMP2 >> ', timestampp)
'''
