import sys
import typing, unittest, numpy, numbers
from typing import Union, Any, List, TypeVar, Callable
from collections.abc import Iterable

def A(B):

    def fun(*args):
        print(B.__name__)
        for i in args:
            print(i)
        return B.__call__()
    return fun

def ret_2():
    return 2

new_fun=A(ret_2)
print(new_fun('blah1', 'blah2', 'blah3', 'blah4'))

# from typing import Callable
#
# def A(B):
#
#     def fun(*args):
#         stuff=[]
#         stuff.append(B.__name__)
#         for i in args:
#             stuff.append(i)
#         return B.__call__()
#     return fun