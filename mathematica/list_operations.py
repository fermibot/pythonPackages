from .mathematical_functions import *
from .core_functions import *


def _promptNotIterable():
    print("The object needs to be iterable\nDas object ist nicht iterierbar")


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


def Length(_list: list):
    return len(_list)


def Union(*args):
    _union = []
    for i in args:
        for j in i:
            if j not in _union:
                _union.append(j)
            elif i in _union:
                _union = _union
    return _union


def Join(*args):
    _join = []
    for i in args:
        for j in i:
            _join.append(j)
    return _join


def Catenate(_list: list):
    _catenate = []
    for i in _list:
        for j in i:
            _catenate.append(j)
    return _catenate


def Rest(_list: list):
    try:
        __list = []
        for i in range(1, len(_list)):
            __list.append(i)
        return __list
    except:
        _promptNotIterable()


def Total(_list: list):
    _total = 0
    for i in _list:
        _total += i
    return _total


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

    # else (not isinstance(obj, str)) or (not isinstance(obj, list)) or (not isinstance(obj, tuple)):
    else:
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


def Partition(_list: list, n):
    if n >= len(_list):
        return _list

    elif n < len(_list):
        _partition = []
        _partitionn = []
        i = 0
        while i < (len(_list) - (len(_list) % n)):
            for r in range(i, i + n):
                _partitionn.append(_list[r])
            _partition.append(_partitionn)
            _partitionn = []
            i += n
        return _partition


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
    return _tuple


def Table(obj):
    # TODO: Add functionality to the function ;)
    pass


def PowerRange(*args):
    if len(args) == 1:
        _powerRange = []
        if NumberQ(args[0]):
            i = 0
            while (10 ** i) <= args[0]:
                _powerRange.append(10 ** i)
                i += 1
            return _powerRange

    elif len(args) == 2:
        i = 0
        _powerRange = []
        while (10 ** i) <= args[1]:
            if (10 ** i >= args[0]) and (10 ** i <= args[1]):
                _powerRange.append(10 ** i)
                i += 1
            else:
                i += 1
        return _powerRange
    elif len(args) == 3:
        i = 0
        _powerRange = []
        while (args[2] ** i) <= args[1]:
            if (args[2] ** i >= args[0]) and (args[2] ** i <= args[1]):
                _powerRange.append(args[2] ** i)
                i += 1
            else:
                i += 1
        return _powerRange


def CirclePoints(*args):
    try:
        if len(args) == 1:
            _circlePoints = []
            for i in range(0, args[0] + 1):
                _circlePoints.append([Sin(2 * i * Pi / args[0]), Cos(2 * i * Pi / args[0])])
            return _circlePoints
        elif len(args) == 2 and NumberQ(args[0]):
            _circlePoints = []
            for i in range(0, args[1] + 1):
                _circlePoints.append([args[0] * Sin(2 * i * Pi / args[1]), args[0] * Cos(2 * i * Pi / args[1])])
            return _circlePoints
        elif len(args) == 2 and ListQ(args[0]):
            _circlePoints = []
            for i in range(0, args[1] + 1):
                _circlePoints.append([
                    args[0][0] * Sin(((2 * i * Pi) + args[0][1]) / args[1]),
                    args[0][0] * Cos(((2 * i * Pi) + args[0][1]) / args[1])
                ])
            return _circlePoints
        elif len(args) == 3 \
                and ListQ(args[0]) \
                and ListQ(args[1]) \
                and NumberQ(args[1][0]) \
                and NumberQ(args[1][1]) \
                and IntegerQ(args[2]):
            _circlePoints = []
            for i in range(0, args[2] + 1):
                _circlePoints.append([
                    (args[1][0] * Sin(((2 * i * Pi) + args[1][1]) / args[2])) + args[0][0],
                    (args[1][1] * Cos(((2 * i * Pi) + args[1][1]) / args[2])) + args[0][1]
                ])
            return _circlePoints
    except TypeError:
        # TODO: Add documentation.
        pass


def Subdivide(*args):
    if len(args) == 1:
        try:
            if IntegerQ(args[0]) and args[0] >= 1:
                _subDivide = []
                for i in range(0, args[0] + 1):
                    _subDivide.append(i / args[0])
                return _subDivide
        except TypeError:
            print("Enter an integer value")
    elif len(args) == 2:
        try:
            if NumberQ(args[0]) and IntegerQ(args[1]) and args[1] >= 1:
                _subDivide = []
                for i in range(0, args[1] + 1):
                    _subDivide.append(i * args[0] / args[1])
                return _subDivide
        except TypeError:
            print("Enter proper arguments")
    elif len(args) == 3:
        try:
            if NumberQ(args[0]) \
                    and NumberQ(args[1]) \
                    and IntegerQ(args[2]) and args[2] >= 1:
                _subDivide = []
                for i in range(0, args[2] + 1):
                    _subDivide.append( args[0] + (i * (args[1] - args[0]) / args[2]))
                return _subDivide
        except TypeError:
            print("")


def CoordinateBoundsArray(*args):
    # TODO: Add tuple type functionality to this implementation
    if len(args) == 1 and ListQ(args[0]):
        _array = []
        xpos = args[0][0][0]
        while xpos <= Floor(args[0][0][1]):
            _arraylet = []
            ypos = args[0][1][0]
            while ypos <= Floor(args[0][1][1]):
                _arraylet.append([xpos, ypos])
                ypos += 1
            _array.append(_arraylet)
            xpos += 1
        return _array

    elif len(args) == 2:
        if ListQ(args[0]) and NumberQ(args[1]):
            pass
        elif ListQ(args[0]) and ListQ(args[1]):
            pass
    elif len(args) == 3:
        pass
    elif len(args) == 4:
        pass


def FindDivisions(*args):
    if len(args) == 2:
        try:
            if ListQ(args[0]) and (len(args[0]) == 2) and IntegerQ(args[1]):
                pass
            elif ListQ(args[0]) and (len(args[0]) == 3) and IntegerQ(args[1]):
                pass
            elif ListQ(args[0]) and ListQ(args[1]):
                pass
            elif ListQ(args[0]) and ListQ(args[1]) and ListQ(Last(args[0])):
                pass
        except TypeError:
            pass
    else:
        pass
        # TODO: Print help document.
        # TODO: Plus, I do not understand what 'Nice Numbers' mean.
        # TODO: Need to re-write the whole function.


def SparseArray(*args):
    if ListQ(args[0]) and len(args) == 1:
        _list = args[0]
        _maxx = 0
        _maxy = 0
        for i in _list:
            if i[0][0] > _maxx:
                _maxx = i[0][0]
                if i[0][1] > _maxy:
                    _maxy = i[0][1]
        _dimensions = Max([_maxx, _maxy])

        _listDict = {}
        for i in _list:
            _listDict.update({str(i[0]): i[1]})

        _sparseArray = []
        for i in range(1, _dimensions + 1):
            for j in range(1, _dimensions + 1):
                if str([i, j]) in _listDict:
                    _sparseArray.append([[i, j], _listDict[str([i, j])]])
                elif str([i, j]) not in _listDict:
                    _sparseArray.append([[i, j], 0])
        return Partition(_sparseArray, _dimensions)

    elif len(args) == 2 and ListQ(args[0]) and ListQ(args[1]):
        if len(args[0]) == len(args[1]):

            _list = args[0]
            _transpose = Transpose(args[0])
            _dimensions = Max([Max(_transpose[0]), Max(_transpose[1])])

            _listDict = {}
            for i in range(0, len(args[0])):
                _listDict.update({str(args[0][i]): args[1][i]})

            _sparseArray = []
            for i in range(1, _dimensions + 1):
                for j in range(1, _dimensions + 1):
                    if str([i, j]) in _listDict:
                        _sparseArray.append([[i, j], _listDict[str([i, j])]])
                    elif str([i, j]) not in _listDict:
                        _sparseArray.append([[i, j], 0])
            return Partition(_sparseArray, _dimensions)
        else:
            print("The two lists need to be of equal lengths")
    else:
        print("No, can't do")
        # TODO: Add documentation


def PadLeft():
    pass


def PadRight(*args):
    if len(args) == 2 and ListQ(args[0]) and NumberQ(args[1]):
        for i in range(0, args[1] - len(args[0])):
            args[0].append(0)
        return args[0]
    elif len(args) == 3 and ListQ(args[0]) and NumberQ(args[1]) and not ListQ(args[2]):
        for i in range(0, args[1] - len(args[0])):
            args[0].append(args[2])
        return args[0]
    elif len(args) == 3 and ListQ(args[0]) and ListQ(args[2]) and NumberQ(args[1]):
        for i in range(0, args[1] - len(args[0])):
            args[0].append(args[2][i % len(args[2])])
        return args[0]
    elif len(args) == 4 and ListQ(args[0]) and NumberQ(args[1]) and NumberQ(args[3]):
        _margin = []
        for i in range(0, args[3]):
            _margin.append(args[2])
        for i in range(0, args[1] - args[3] - len(args[0])):
            args[0].append(args[2])
        return Join(_margin, args[0])
    elif len(args) == 2 and ListQ(args[0]) and ListQ(args[1]):
        pass
    elif len(args) == 1 and ListQ(args[0]):
        pass


def ArrayReshape(_list: list):
    return _list


def Fibonacci(n):
    _a = 0
    _b = 1
    _i = 1
    while _i < n:
        _temp = _b
        _b += _a
        _a = _temp
        _i += 1
    return _b


def Tribonacci(n):
    _a = 0
    _b = 0
    _c = 1
    _i = 1
    while _i < n:
        _temp1 = _b
        _temp2 = _c
        _c = _c + _b + _a
        _a = _temp1
        _b = _temp2
        _i += 1
    return _c


def Quadranacci(n):
    _a = 0
    _b = 0
    _c = 0
    _d = 1
    _i = 1
    while _i < n:
        _temp1 = _b
        _temp2 = _c
        _temp3 = _d
        _d = _d + _c + _b + _a
        _a = _temp1
        _b = _temp2
        _c = _temp3
        _i += 1
    return _d


def Pentonacci(n):
    _a = 0
    _b = 0
    _c = 0
    _d = 0
    _e = 1
    _i = 1
    while _i < n:
        _temp1 = _b
        _temp2 = _c
        _temp3 = _d
        _temp4 = _e
        _e = _e + _d + _c + _b + _a
        _a = _temp1
        _b = _temp2
        _c = _temp3
        _d = _temp4
        _i += 1
    return _e


def Hexonacci(n):
    _a = 0
    _b = 0
    _c = 0
    _d = 0
    _e = 0
    _f = 1
    _i = 1
    while _i < n:
        _temp1 = _b
        _temp2 = _c
        _temp3 = _d
        _temp4 = _e
        _temp5 = _f
        _f = _f + _e + _d + _c + _b + _a
        _a = _temp1
        _b = _temp2
        _c = _temp3
        _d = _temp4
        _e = _temp5
        _i += 1
    return _f


def Polynacci(n: int, base: int):
    _polynacci = [1]
    for i in range(0, base):
        _polynacci.append(2 ** i)
    if n <= base:
        return _polynacci[n - 1]
    elif n > base:
        _len = len(_polynacci)
        while _len < n + 1:
            _polynacci.pop(0)
            _polynacci.append(Total(_polynacci))
            _len += 1
        return _polynacci[-1]


def Riffle(*args):
    if len(args) == 2:
        if ListQ(args[0]) and not ListQ(args[1]):
            _riffle = []
            for i in args[0]:
                _riffle.append(i)
                _riffle.append(args[1])
            _riffle.pop((len(_riffle) - 1))
            return _riffle
        elif ListQ(args[0]) and ListQ(args[1]):
            _riffle = []
            _len = len(args[1])
            for i in range(0, len(args[0])):
                _riffle.append(args[0][i])
                _riffle.append(args[1][i % _len])
            _riffle.pop(len(_riffle) - 1)
            return _riffle

    elif len(args) == 3:
        if ListQ(args[0]) and NumberQ(args[2]):
            _riffle = []
            for i in range(len(args[0])):
                _riffle.append(args[0][i])
                pass
        elif ListQ(args[0]) and ListQ(args[2]):
            pass
    else:
        pass


def Binlists(*args):
    if len(args) == 1:
        _max = Max(args[0])
        _min = Min(args[0])
        _binLists = []
        return _binLists


def Append(_list, _element):
    _list.append(_element)
    return _list


def Prepend(_list, _element):
    _list.insert(0, _element)
    return _list


def ConstantArray(*args):

    def _constantArrayHelp(_obj, _number):
        _constantArrayHelp = []
        for i in range(0, Ceiling(_number)):
            _constantArrayHelp.append(_obj)
        return _constantArrayHelp

    if len(args) == 2:
        if NumberQ(args[1]):
            _constantArray = []
            for i in range(0, Round(args[1])):
                _constantArray.append(args[0])
            return _constantArray

        if ListQ(args[1]):
            _obj = args[0]
            for i in args[1]:
                _obj = _constantArrayHelp(_obj, i - 1)
            return _obj
    else:
        pass