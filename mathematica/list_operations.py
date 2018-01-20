

def Range(i, j=None, step=None):
    # TODO : add functionality for non integer steps
    i = int(i)
    if step is None:
        if j is None:
            if i < 1:
                return 0
            elif i >= 1:
                sample = []
                for i in range(0, i):
                    sample.append(i + 1)
                return sample
        if j is not None:
            if i < 1:
                return 0
            elif i >= 1:
                sample = []
                for i in range(i, j + 1):
                    sample.append(i + 1)
                return sample
    elif step is not None:
        if i < 1:
            return 0
        elif i >= 1:
            sample = []
            for i in range(i, j + 1):
                i += step
                sample.append(i)
            return sample


def Head(obj):
    return type(obj)


def First(_list: list):
    return _list[0]


def Last(_list: list):
    _len = len(_list)
    return _list[_len - 1]


def Rest(_list:list):
    __list = []
    for i in range(1, len(_list)):
        __list.append(i)
    return __list


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

