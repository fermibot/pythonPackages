from .q_functions import *


def Range(i, j=None, step=None):
    def _Range(_lower, _upper, _step):
        __elem, __list = _lower, []
        while __elem <= _upper:
            __list.append(__elem)
            __elem += _step
        return __list

    if step is None:
        if j is None:
            if i <= 0:
                return 0
            elif i >= 1:
                return _Range(1, i, 1)
        elif j is not None:
            if j < i:
                print("Upper limit needs to be smaller than the lower limit.")
            elif i == j:
                return i
            elif i < j:
                return _Range(i, j, 1)
    elif step is not None:
        diff = j - i
        if diff < 0:
            print("Upper limit needs to be smaller than the lower limit.")
        elif diff == 0:
            return i
        elif diff > 0:
            return _Range(i, j, step)


def Factorial(x):
    if x == 0:
        return 1
    if (not isinstance(x, int)) or (x < 1):
            return "Non integer functionality not yet included"
    elif (isinstance(x, int)) and (x >= 1):
        _fact = 1
        for i in range(1, x + 1):
            _fact = _fact * i
        return _fact


def Factorial2(x):
    _factorial2 = 1
    if x == 0:
        return _factorial2
    elif EvenQ(x):
        for i in range(1, int(x / 2) + 1):
            _factorial2 = _factorial2 * i * 2
    elif OddQ(x):
        for i in range(1, int((x  + 1)/ 2) + 1):
            _factorial2 *= (2 * i - 1)
    return _factorial2