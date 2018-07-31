from .q_functions import *


def Print(_obj):
    print(_obj)


def Max(_list: list):
    _max = _list[0]
    for i in _list:
        if i > _max:
            _max = i
        else:
            _max = _max
    return _max


def Min(_list: list):
    _min = _list[0]
    for i in _list:
        if i < _min:
            _min = i
        else:
            _min = _min
    return _min


def promptReal():
    print("Input needs to be a real number \nDie Eingabe muss eine reelle Zahl sein")


def Abs(x: float):
    try:
        if x >= 0:
            _x = x
        elif x <= 0:
            _x = -1 * x
        return _x
    except TypeError:
        promptReal()
        # TODO: This prints a redundant none statement.


def Sign(_x):
    if _x < 0:
        return -1
    elif _x > 0:
        return 1


def Greater(_list):
    if len(_list) == 2:
        return _list[0] > _list[1]
    elif len(_list) > 2:
        _greater = True
        for i in range(0, len(_list)):
            _greater = _greater and (_list[i] > _list[i + 1])
            return _greater


def GreaterEqual(_list):
    if len(_list) == 2:
        return _list[0] >= _list[1]
    elif len(_list) > 2:
        _greaterEqual = True
        for i in range(0, len(_list)):
            _greaterEqual = _greaterEqual and (_list[i] >= _list[i + 1])
            return _greaterEqual


def Less(_list):
    if len(_list) == 2:
        return _list[0] < _list[1]
    elif len(_list) > 2:
        _less = True
        for i in range(0, len(_list)):
            _less = _less and (_list[i] < _list[i + 1])
            return _less


def LessEqual(_list):
    if len(_list) == 2:
        return _list[0] <= _list[1]
    elif len(_list) > 2:
        _lessEqual = True
        for i in range(0, len(_list)):
            _lessEqual = _lessEqual and (_list[i] >= _list[i + 1])
            return _lessEqual


def LessThanAll(element, _list:list):
    truth = True
    for i in _list:
        truth = (element < i) and truth
    return truth


def LessThanEqualToAll(element, _list:list):
    truth = True
    for i in _list:
        truth = (element <= i) and truth
    return truth


def GreaterThanAll(element, _list:list):
    truth = True
    for i in _list:
        truth = (element > i) and truth
    return truth


def GreaterThanEqualToAll(element, _list:list):
    truth = True
    for i in _list:
        truth = (element >= i) and truth
    return truth



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
        for i in range(1, int((x + 1) / 2) + 1):
            _factorial2 *= (2 * i - 1)
    return _factorial2


def Binomial(_n, _m):
    _n, _m = Abs(_n), Abs(_m)
    return Factorial(_n) / (Factorial(_n - _m) * Factorial(_m))


def Boole(_obj):
    if _obj:
        return 1
    elif not _obj:
        return 0