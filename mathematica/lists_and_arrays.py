from .mathematical_functions import *
# from .core_functions import *
from .precision import *


def promptNotIterable():
    print("The object needs to be iterable\nDas object ist nicht iterierbar")


def Head(obj):
    return type(obj)


def First(_list: list):
    try:
        return _list[0]
    except TypeError:
        promptNotIterable()


def Last(_list: list):
    try:
        _len = len(_list)
        return _list[_len - 1]
    except TypeError:
        promptNotIterable()


def Length(_list: list):
    return len(_list)


def _longestSubList(_list: list):
    _max = Length(_list[0])
    for i in _list:
        if Length(i) > _max:
            _max = Length(i)
        else:
            _max = _max
    return _max


def _shortestSubList(_list):
    _min = Length(_list[0])
    for i in _list:
        if Length(i) < _min:
            _min = Length(i)
        else:
            _min = _min
    return _min


def _arrayGenerator(_list: list, n: int):
    arrayGenerator = []
    for i in range(0, n):
        arrayGenerator.append(_list)
    return arrayGenerator


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
    except TypeError:
        promptNotIterable()


def Total(_list: list):
    _total = 0
    for i in _list:
        _total += i
    return _total


def Accumulate(_list: list):
    _accumulate = [First(_list)]
    _element = First(_list)
    for i in range(1, Length(_list)):
        _element += _list[i]
        _accumulate.append(_element)
    return _accumulate


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
        promptNotIterable()


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


def ArrayReshape(_list: list, _reshape: list):
    _length = Length(_list)
    for i in Reverse(_reshape):
        _list = Partition(_list, _length * int(Reciprocal(i)))
    return _list


def CenterArray(*args):
    def _centerArrayAssist(*_args):
        # _args[0] = element
        # _args[1] = length
        # _args[2] = padding
        __centerArray = ConstantArray(_args[2], _args[1])
        if EvenQ(_args[1]):
            __centerArray[int(_args[1] // 2) - 1] = _args[0]
        elif OddQ(_args[1]):
            __centerArray[int(_args[1] // 2)] = _args[0]
        return __centerArray

    def _findCenter(n):
        if OddQ(n):
            return n // 2
        elif EvenQ(n):
            return n // 2 - 1

    _findCenter(2)

    if len(args) == 2 and not ListQ(args[1]):
        return _centerArrayAssist(args[0], args[1], 0)
    elif len(args) == 2 and ListQ(args[1]):
        _centerArray = ConstantArray(0, Last(args[1]))
        for i in range(1, Length(args[1])):
            _centerArray = _arrayGenerator(_centerArray, args[1][i])
        # _arrayIndex = '_centerArray'
        # for i in args[1]:
        #     _arrayIndex += '[' + str(_findCenter(i)) + ']'
        # _arrayIndex += ' = 2'
        # _centerArray = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0],
        # [0, 0, 0]]]
        exec('_centerArray[1][1][1] = 1')
        return _centerArray
    elif len(args) == 3:
        return _centerArrayAssist(args[0], args[1], args[2])
    elif len(args) == 1:
        return _centerArrayAssist(1, args[0], 0)


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
    return obj


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
                    _subDivide.append(args[0] + (i * (args[1] - args[0]) / args[2]))
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

            # added # for PEP warning elimination _list = args[0]
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


def _padSimpleLeft(_list: list, _padding, _element):
    __padSimpleLeft = []
    if _padding > len(_list):
        for i in range(0, _padding - len(_list)):
            __padSimpleLeft.append(_element)
        return Join(__padSimpleLeft, _list)
    elif len(_list) == _padding:
        return _list
    elif _padding < len(_list):
        return _list[len(_list) - _padding: len(_list):]


def PadLeft(*args):
    if len(args) == 2 and ListQ(args[0]) and not ListQ(args[1]) and NumberQ(args[1]):
        return _padSimpleLeft(args[0], args[1], 0)
    elif len(args) == 3 and ListQ(args[0]) and NumberQ(args[1]) and not ListQ(args[2]):
        return _padSimpleLeft(args[0], args[1], args[2])
    elif len(args) == 3 and NumberQ(args[1]) and ListQ(args[2]):
        if len(args[0]) >= args[1]:
            return _padSimpleLeft(args[0], args[1], "")
        elif len(args[0]) < args[1]:
            _leftPad = []
            for i in range(0, args[1] - len(args[0])):
                _leftPad.append(args[2][i % len(args[2])])
            return Join(_leftPad, args[0])
    elif len(args) == 4 and NumberQ(args[1]) and NumberQ(args[3]):
        if len(args[0]) >= args[1] + args[3]:
            return _padSimpleLeft(args[0], args[1], "")
        elif len(args[0]) < args[1] + args[3]:
            _margin = []
            for i in range(0, args[3]):
                _margin.append(args[2])
            _notMargin = []
            for i in range(0, args[1] - args[3] - len(args[0])):
                _notMargin.append(args[2])
            return Join(_notMargin, args[0], _margin)
    elif len(args) == 2 and ListQ(args[0]) and ListQ(args[1]):
        pass
    elif len(args) == 1 and ListQ(args[0]):
        _max = _longestSubList(args[0])
        _padLeft = []
        for i in args[0]:
            _padLeft.append(_padSimpleLeft(i, _max, 0))
        return _padLeft


def _padSimpleRight(_list: list, _padding, _element):
    if len(_list) >= _padding:
        __padSimpleRight = []
        for i in range(0, _padding):
            __padSimpleRight.append(_list[i])
        return __padSimpleRight
    elif len(_list) < _padding:
        for i in range(0, _padding - len(_list)):
            _list.append(_element)
        return _list


def PadRight(*args):
    if len(args) == 2 and ListQ(args[0]) and NumberQ(args[1]):
        return _padSimpleRight(args[0], args[1], 0)
    elif len(args) == 3 and ListQ(args[0]) and NumberQ(args[1]) and not ListQ(args[2]):
        return _padSimpleRight(args[0], args[1], args[2])
    elif len(args) == 3 and ListQ(args[0]) and ListQ(args[2]) and NumberQ(args[1]):
        if len(args[0]) >= args[1]:
            return _padSimpleRight(args[0], args[1], "")
        elif len(args[0]) < args[1]:
            for i in range(0, args[1] - len(args[0])):
                args[0].append(args[2][i % len(args[2])])
            return args[0]
    elif len(args) == 4 and ListQ(args[0]) and NumberQ(args[1]) and NumberQ(args[3]):
        if len(args[0]) >= args[1] + args[3]:
            return _padSimpleRight(args[0], args[1], "")
        elif len(args[0]) < args[1] + args[3]:
            _margin = []
            for i in range(0, args[3]):
                _margin.append(args[2])
            for i in range(0, args[1] - args[3] - len(args[0])):
                args[0].append(args[2])
            return Join(_margin, args[0])
    elif len(args) == 2 and ListQ(args[0]) and ListQ(args[1]):
        pass
    elif len(args) == 1 and ListQ(args[0]):
        _max = _longestSubList(args[0])
        _padRight = []
        for i in args[0]:
            _padRight._padSimpleRight(i, _max, 0)
        return _padRight


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
        _binLists = [_min, _max]
        return _binLists


def Append(_list, _element):
    _list.append(_element)
    return _list


def Prepend(_list, _element):
    _list.insert(0, _element)
    return _list


def ConstantArray(*args):
    def constantArrayHelp(_obj, _number):
        _constantArrayHelp = []
        for _i in range(0, Ceiling(_number)):
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
                _obj = constantArrayHelp(_obj, i - 1)
            return _obj
    else:
        pass


def KroneckerDelta(*args):
    _kroneckerDelta = True
    for i in range(1, len(args)):
        _kroneckerDelta = _kroneckerDelta and (args[i - 1] == args[i])
    if _kroneckerDelta:
        return 1
    else:
        return 0


# Matrices
def BoxMatrix(*args):
    _boxMatrix = []
    if len(args) == 1 and not ListQ(args[0]):
        for i in range(-args[0], args[0] + 1):
            _boxRow = []
            for j in range(-args[0], args[0] + 1):
                _boxRow.append(1)
            _boxMatrix.append(_boxRow)
        return _boxMatrix
    elif len(args) == 2:
        _limit = args[0]
        for i in range(-args[1], args[1] + 1):
            _boxRow = []
            for j in range(-args[1], args[1] + 1):
                if (-_limit <= j <= _limit) and (-_limit <= i <= _limit):
                    _boxRow.append(1)
                else:
                    _boxRow.append(0)
            _boxMatrix.append(_boxRow)
        return _boxMatrix
    elif len(args) == 1 and ListQ(args[0]):
        _list = Reverse(args[0])
        _boxMatrix = ConstantArray(1    , 2 * First(_list) + 1)
        for i in range(1, len(_list)):
            _boxMatrix = _arrayGenerator(_boxMatrix, 2 * _list[i] + 1)
        return _boxMatrix


# EXPERIMENTAL
#
#
# def _listBuilder(_list: list, _n: int):
#     _listBuilder = []
#     for i in range(0, _n):
#         _listBuilder.append(_list)
#     return _listBuilder
#
#
# _list = Range(5)
# for i in ConstantArray(5, 3):
#     _list = _listBuilder(_list, i)
#
# print(_list)
#
#
# def levelAnalyzer(_list: list):
#     _list = str(_list)
#     _elements = Union(Characters(_list))
#     _filteredElements = []
#     for i in _elements:
#         if i not in ('[', ']'):
#             _filteredElements.append(i)
#     for i in _filteredElements:
#         _list = _list.replace(i, '')
#
#     _count = 0
#     _bracket = '['
#     _countList = []
#     for i in _list:
#         if i == _bracket:
#             _count += 1
#         else:
#             _countList.append(_count)
#             _count = 0
#     return _countList
#
# print(levelAnalyzer(_list))
