from mathematica.calculus import *
from mathematica.list_operations import *
from mathematica.mathematical_functions import *
from mathematica.precision import *
from mathematica.q_functions import *
from mathematica.random_functions import *


def _promptNotIterable():
    print("The object needs to be iterable\nDas object ist nicht iterierbar")


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


def Head(obj):
    return type(obj)


def First(_list: list):
    try:
        return _list[0]
    except TypeError:
        _promptNotIterable()


def Last(_list: list):
    try:
        _len = len(_list)
        return _list[_len - 1]
    except TypeError:
        _promptNotIterable()


def Rest(_list: list):
    try:
        __list = []
        for i in range(1, len(_list)):
            __list.append(i)
        return __list
    except:
        _promptNotIterable()


def Reverse(obj):
    if isinstance(obj, str):
        _obj = ""
        for i in reversed(obj):
            _obj += i
        return _obj
    elif isinstance(obj, list):
        _obj = []
        for i in reversed(obj):
            _obj.append(i)
        return _obj
    elif isinstance(obj, tuple):
        _obj = []
        for i in reversed(obj):
            _obj.append(i)
    elif isinstance(obj, range):
        _obj = []
        for i in reversed(obj):
            _obj.append(i)
        return _obj

    elif (not isinstance(obj, str)) or (isinstance(obj, list)) or isinstance(obj, tuple):
        _promptNotIterable()
        # TODO: Else returns none, check with Gowtham


def Transpose(_list: list):
    _transpose = []
    for i in range(0, len(_list[0])):
        _transposelet = []
        for j in range(0, len(_list)):
            _transposelet.append(_list[j][i])
        _transpose.append(_transposelet)
    return _transpose


def Tuples(_list: list, level: int):
    l = len(_list)
    _tuple = []
    for n in range(0, level):
        _tuplet = []
        for j in range(0, l ** n):
            _tuplett = []
            for r in range(0, l):
                _tuplettt = []
                for k in range(0, l ** (level - n - 1)):
                    _tuplettt += [_list[r]]
                _tuplett += _tuplettt
            _tuplet += _tuplett
        _tuple.append(_tuplet)
    _tuple = Transpose(_tuple)
    for r in _tuple:
        print(r)


def Table(obj):
    # TODO: Add functionality to the function ;)
    pass


def CirclePoints(*kwargs):
    try:
        if len(kwargs) == 1:
            _circlePoints = []
            for i in range(0, kwargs[0] + 1):
                _circlePoints.append([Sin(2 * i * Pi / kwargs[0]), Cos(2 * i * Pi / kwargs[0])])
            return _circlePoints
        elif len(kwargs) == 2 and NumberQ(kwargs[0]):
            _circlePoints = []
            for i in range(0, kwargs[1] + 1):
                _circlePoints.append([kwargs[0] * Sin(2 * i * Pi / kwargs[1]), kwargs[0] * Cos(2 * i * Pi / kwargs[1])])
            return _circlePoints
        elif len(kwargs) == 2 and ListQ(kwargs[0]):
            _circlePoints = []
            for i in range(0, kwargs[1] + 1):
                _circlePoints.append([
                    kwargs[0][0] * Sin(((2 * i * Pi) + kwargs[0][1]) / kwargs[1]),
                    kwargs[0][0] * Cos(((2 * i * Pi) + kwargs[0][1]) / kwargs[1])
                ])
            return _circlePoints
        elif len(kwargs) == 3 \
                and ListQ(kwargs[0]) \
                and ListQ(kwargs[1]) \
                and NumberQ(kwargs[1][0]) \
                and NumberQ(kwargs[1][1]) \
                and IntegerQ(kwargs[2]):
            _circlePoints = []
            for i in range(0, kwargs[2] + 1):
                _circlePoints.append([
                    (kwargs[1][0] * Sin(((2 * i * Pi) + kwargs[1][1]) / kwargs[2])) + kwargs[0][0],
                    (kwargs[1][1] * Cos(((2 * i * Pi) + kwargs[1][1]) / kwargs[2])) + kwargs[0][1]
                ])
            return _circlePoints
    except TypeError:
        # TODO: Add command list
        pass


def Subdivide(*kwargs):
    if len(kwargs) == 1:
        try:
            if IntegerQ(kwargs[0]) and kwargs[0] >= 1:
                _subDivide = []
                for i in range(0, kwargs[0] + 1):
                    _subDivide.append(i / kwargs[0])
                return _subDivide
        except TypeError:
            print("Enter an integer value")
    elif len(kwargs) == 2:
        try:
            if NumberQ(kwargs[0]) and IntegerQ(kwargs[1]) and kwargs[1] >= 1:
                _subDivide = []
                for i in range(0, kwargs[1] + 1):
                    _subDivide.append(i * kwargs[0] / kwargs[1])
                return _subDivide
        except TypeError:
            print("Enter proper arguments")
    elif len(kwargs) == 3:
        try:
            if NumberQ(kwargs[0]) \
                    and NumberQ(kwargs[1]) \
                    and IntegerQ(kwargs[2]) and kwargs[2] >= 1:
                _subDivide = []
                for i in range(0, kwargs[2] + 1):
                    _subDivide.append( kwargs[0] + (i * (kwargs[1] - kwargs[0]) / kwargs[2]))
                return _subDivide
        except TypeError:
            print("")


def CoordinateBoundsArray(*kwargs):
    if len(kwargs) == 1 and ListQ(kwargs[0]):
        _array = []
        xpos = kwargs[0][0][0]
        while xpos <= Floor(kwargs[0][0][1]):
            _arraylet = []
            ypos = kwargs[0][1][0]
            while ypos <= Floor(kwargs[0][1][1]):
                _arraylet.append([xpos, ypos])
                ypos += 1
            _array.append(_arraylet)
            xpos += 1
        return _array

    elif len(kwargs) == 2:
        if ListQ(kwargs[0]) and NumberQ(kwargs[1]):
            pass
        elif ListQ(kwargs[0]) and ListQ(kwargs[1]):
            pass
    elif len(kwargs) == 3:
        pass
    elif len(kwargs) == 4:
        pass