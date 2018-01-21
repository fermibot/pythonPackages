def Range(i, j=None, step=None):

    def _Range( _lower, _upper, _step):
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
            elif i ==j:
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
        print("The object is not iterable")
        print("Das object ist nicht iterierbar")


def Last(_list: list):
    try:
        _len = len(_list)
        return _list[_len - 1]
    except TypeError:
        print("The object is not iterable")
        print("Das objekt ist nicht iterierbar")


def Rest(_list:list):
    try:
        __list = []
        for i in range(1, len(_list)):
            __list.append(i)
        return __list
    except:
        print("The object is not iterable")
        print("Das objekt ist nicht iterierbar")


def Reverse(_list: list):
    __list = []
    for i in reversed(_list):
        __list.append(i)
    return __list


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
        for j in range(0, l**n):
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
