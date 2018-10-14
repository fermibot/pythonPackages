from mathematica.random_functions import *

_megaList = []
for i in range(100):
    _total = 0
    _list = []
    while True:
        _rand = RandomReal(0, 1)
        if _total + _rand <= 1:
            _list.append(_rand)
            _total += _rand
        else:
            _list.append(1 - _total)
            break
    _megaList.append(_list)

print(_megaList)
