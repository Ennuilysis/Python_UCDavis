import copy
from typing import Generator

x = []


def re_fun(given: str, answer: str = ""):
    if given == '':
        x.append(copy.deepcopy(answer))
    elif given[0] == "X":
        re_fun(given[1:], answer + "0")
        re_fun(given[1:], answer + "1")
    else:
        re_fun(given[1:], answer + given[0])


def binary_strings(string: str) -> Generator[str, None, None]:
    # try:
    #     string.index("X")
    # except:
    #     return string
    re_fun(string)
    yield from x


d = ((binary_strings("11")))
print(next(d))
