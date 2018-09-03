from mathematica.random_functions import *
from mathematica.lists import *
from mathematica.monitoring import *
from mathematica.sheldon_ross_problems.sheldon_ross_utilities import *


_neutronPaths = []
for i in range(0, 10):
    _seed = RandomReal(0, 1)
    _seedList = [_seed]
    while 0 <= _seed <= 10:
        _seed += RandomReal(-1, 1)
        _seedList.append(_seed)
        if _seedList.__len__() > 10:
            break
        _neutronPaths.append(_seedList)

print(_neutronPaths)