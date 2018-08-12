from mathematica.random_functions import *
from mathematica.lists import *

for i in range(100):
    _randomList = [RandomReal()]
    _randomElement = RandomReal()
    while LessThanAll(_randomElement, _randomList):
        _randomList.append(_randomElement)
    print(_randomList)
