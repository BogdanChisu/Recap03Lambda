"""
--------------------------------------------------
LAMBDA EXPRESSIONS
--------------------------------------------------

What is a lambda expression?
--------------------------------------------------

The lambda expression is an anonymous function. It is a function that has no name and is defined where it
is used. It does not include the keyword def.

Instead the keyword lambda is used followed by:
- a comma-separated list of arguments
- a colon
- a single expression that returns the value of the function


Examples:
--------------------------------------------------
"""
# 1
my_lambda = lambda x: x.lower()
print(my_lambda("HA HA HA")) # "ha ha ha"
"""
The above is a simplified notation of the traditional function:
"""
def my_lambda(x):
    return x.lower()

# 2
square_lambda = lambda x: x ** 2
print(square_lambda(4)) # 16

# 3
equals_lambda = lambda x, y: x == y
print(equals_lambda(1, 2)) # False

"""
APPLICATION
--------------------------------------------------

We must bear in mind that the use of lambda affects the readability of the code

map
--------------------------------------------------
"""
items = [1, 2, 3, 4, 5]
squared = list(map(lambda  x: x ** 2, items)) # [1, 4, 9, 16, 25]
print(squared)

"""
filter
--------------------------------------------------
"""
odds = list(filter(lambda x: x % 2, items))
print(odds)

"""
function reduce
--------------------------------------------------

The reduce function processes the elements of a collection from left to right as described in the lambda
expression, and produces a single value. The collection is reduced to a single value. In the first step,
the function operates on the first two elements of the collection and returns the result of the
transformation, then it is rerun: for the result achieved in the previous step and the next value from
the list. The process continues as long as there are still items in the list.
"""

from functools import reduce
items_sum = reduce(lambda x, y: x + y, items) # 15
print(f"Suma elementelor: {items_sum}")

"""
function sorted
--------------------------------------------------

We would like to sort the list below, based on the value in the second position
"""
pairs = [(1, 10), (2, 9), (3, 8)]
print(sorted(pairs, key=lambda x: x[1])) # [(3, 8), (2, 9), (1, 10)]
"""
function min and max
--------------------------------------------------
"""
print(min(pairs)) # (1, 10)
print(max(pairs, key=lambda x: x[1])) # (1, 10)
print(max(pairs, key=lambda x: x[0])) # (3, 8)