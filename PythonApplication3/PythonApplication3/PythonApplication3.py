import math

def umnoj(ls):
    x = 1
    for item in ls:
        x = x * item
    print(x)


def dict_str(di):
    dic = dict()
    for key, values in di.items():
        dic[str(key)] = values
    print(dic)

def sort_int(ls):
    if all(isinstance(x, int) for x in ls):
        print(sorted(ls))
    else:
        raise ValueError('You have strings !')


def exception(a, b):
    try:
        print(math.sqrt(a))
    except ValueError as e1:
        print(e1.with_traceback)
    try:
        print(1 / b)
    except TypeError as e2:
        print(e2.with_traceback)
    try:
        raise RuntimeError
    except RuntimeError as e3:
        print(e3.with_traceback)
    
exception(-10, 'asd')

l = [4, 51, 23, 525, ]

sort_int(l)

d = {12: 'python', 45: 'c#', 32: 'java'}

dict_str(d)

umnoj([1, 2, 3, 4])