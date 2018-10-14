from mathematica.random_functions import RandomChoice, RandomInteger
from mathematica.lists import MemberQ

_list = []
_truth = True
_i = 1

while _truth:
    if _i == 5:
        _list.append(5)
    elif _i < 6:
        _rand = RandomChoice([1, 2, 3, 4, 6])
        _list.append(_rand)
    elif _i > 6:
        _rand = RandomInteger(1, 6)
        if _rand != 6:
            _list.append(_rand)
        else:
            _list.append(_rand)
            break
    _i = _i + 1
    print(_list)
