# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# variables in functions are scoped
# variables outside functions have global scope

# Define > def is function in Python
# ====================================


def sayHello():
    print('Hello')


sayHello()
# Hello

# Parameters
# ====================================


def sayHelloo(name):
    print('Hello ' + name)


sayHelloo('Javed')
# Hello Javed

# Default Parameter
# =====================================


def sayHellooo(name='Sam'):
    print('Hello ' + name)


sayHellooo()
# Hello Sam

# Comment Convention
# ======================================


def sayHelloooo(name='Javed Khalil'):
    """
    Prints Hello and then name.
    """
    print('Hello ' + name)


sayHelloooo()
# Hello Javed Khalil

# Return Value
# =====================================


def getSum(num1, num2):
    total = num1 + num2
    return total


print(getSum(2, 5))
# 7
# or
numSum = getSum(6, 5)
print(numSum)
# 11

# Return and Increment
# =====================================


def Sum(numm):
    # numm = numm + 1
    # or
    numm += 1
    return numm


print(Sum(20))
# 21


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

# No return statement needed
# =============================================

# getSm = lambda num1, num2 : num1 + num2
# or
def getSm(num1, num2): return num1 + num2


print(getSm(6, 3))
# 9

# ==============================
# addOne = lambda num : num + 1


def addOne(num): return num + 1


print(addOne(15))
# 16
