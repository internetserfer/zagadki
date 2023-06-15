from argparse import ZERO_OR_MORE
from xml.dom import SyntaxErr


list1 = [1, 2, 3, 4, ]

try:
    list1[9]
except IndexError as e:
    print('Out of range ', e)

try:
    raise TypeError('Wrong type')
except TypeError as e:
    print('Wrong! ', e)

a = 3
b = 6 
try:
    print(2 / a)
except ZeroDivisionError as e:
    print('Wrong! ', e)
finally:
    print('Nope ')


def my_function (val1, val2):
    print(val1 + val2)


my_function(a, b)