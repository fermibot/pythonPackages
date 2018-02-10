from mathematica.load_all_functions import *


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


def Union(*kwargs):
    _union = []
    for i in kwargs:
        for j in i:
            if j not in _union:
                _union.append(j)
            elif i in _union:
                _union = _union
    return _union


def Join(*kwargs):
    _join = []
    for i in kwargs:
        for j in i:
            _join.append(j)
    return _join


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


def PowerRange(*kwargs):
    if len(kwargs) == 1:
        _powerRange = []
        if NumberQ(kwargs[0]):
            i = 0
            while (10 ** i) <= kwargs[0]:
                _powerRange.append(10 ** i)
                i += 1
            return _powerRange

    elif len(kwargs) == 2:
        i = 0
        _powerRange = []
        while (10 ** i) <= kwargs[1]:
            if (10 ** i >= kwargs[0]) and (10 ** i <= kwargs[1]):
                _powerRange.append(10 ** i)
                i += 1
            else:
                i += 1
        return _powerRange
    elif len(kwargs) == 3:
        i = 0
        _powerRange = []
        while (kwargs[2] ** i) <= kwargs[1]:
            if (kwargs[2] ** i >= kwargs[0]) and (kwargs[2] ** i <= kwargs[1]):
                _powerRange.append(kwargs[2] ** i)
                i += 1
            else:
                i += 1
        return _powerRange


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
        # TODO: Add documentation.
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
    # TODO: Add tuple type functionality to this implementation
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


def FindDivisions(*kwargs):
    if len(kwargs) == 2:
        try:
            if ListQ(kwargs[0]) and (len(kwargs[0]) == 2) and IntegerQ(kwargs[1]):
                pass
            elif ListQ(kwargs[0]) and (len(kwargs[0]) == 3) and IntegerQ(kwargs[1]):
                pass
            elif ListQ(kwargs[0]) and ListQ(kwargs[1]):
                pass
            elif ListQ(kwargs[0]) and ListQ(kwargs[1]) and ListQ(Last(kwargs[0])):
                pass
        except TypeError:
            pass
    else:
        pass
        # TODO: Print help document.
        # TODO: Plus, I do not understand what 'Nice Numbers' mean.
        # TODO: Need to re-write the whole function.


def SparseArray(*kwargs):
    if ListQ(kwargs[0]) and len(kwargs) == 1:
        _list = kwargs[0]
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

    elif len(kwargs) == 2 and ListQ(kwargs[0]) and ListQ(kwargs[1]):
        if len(kwargs[0]) == len(kwargs[1]):

            _list = kwargs[0]
            _transpose = Transpose(kwargs[0])
            _dimensions = Max([Max(_transpose[0]), Max(_transpose[1])])

            _listDict = {}
            for i in range(0, len(kwargs[0])):
                _listDict.update({str(kwargs[0][i]): kwargs[1][i]})

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


def Riffle(*kwargs):
    if len(kwargs) == 2:
        if ListQ(kwargs[0]) and not ListQ(kwargs[1]):
            _riffle = []
            for i in kwargs[0]:
                _riffle.append(i)
                _riffle.append(kwargs[1])
            _riffle.pop((len(_riffle) - 1))
            return _riffle
        elif ListQ(kwargs[0]) and ListQ(kwargs[1]):
            _riffle = []
            _len = len(kwargs[1])
            for i in range(0, len(kwargs[0])):
                _riffle.append(kwargs[0][i])
                _riffle.append(kwargs[1][i % _len])
            _riffle.pop(len(_riffle) - 1)
            return _riffle

    elif len(kwargs) == 3:
        if ListQ(kwargs[0]) and NumberQ(kwargs[2]):
            _riffle = []
            for i in range(len(kwargs[0])):
                _riffle.append(kwargs[0][i])
                pass
        elif ListQ(kwargs[0]) and ListQ(kwargs[2]):
            pass
    else:
        pass


# String Operations
def StringJoin(*kwargs):
    def _subStringJoin(obj):
        if not ListQ(obj):
            return str(obj)
        elif ListQ(obj):
            _stringList = ""
            for i in obj:
                _stringList += str(i)
            return _stringList
    if len(kwargs) == 1:
        return _subStringJoin(kwargs[0])
    elif len(kwargs) > 1:
        _stringJoin = []
        for i in kwargs:
             _stringJoin.append(_subStringJoin(i))
        return _stringJoin


def ToString(*kwargs):
    def _subToString(obj):
        if not ListQ(obj):
            return str(obj)
        elif ListQ(obj):
            _stringList = []
            for i in obj:
                _stringList.append(str(i))
            return _stringList
    if len(kwargs) == 1:
        return _subToString(kwargs[0])
    elif len(kwargs) > 1:
        _toString = []
        for i in kwargs:
            _toString.append(_subToString(i))
        return _toString


