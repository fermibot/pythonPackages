
def _promptReal():
    print("Input needs to be a real number \nDie Eingabe muss eine reelle Zahl sein")

def ListQ(obj):
    return isinstance(obj, list) or isinstance(obj, range)


def allListQ(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and ListQ(i)
    return _truth


def TupleQ(obj):
    return isinstance(obj, tuple)


def allTuple(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and TupleQ(i)
    return _truth


def IntegerQ(obj):
    return isinstance(obj, int)


def allIntegerQ(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and IntegerQ(i)
    return _truth


def FloatQ(obj):
    return isinstance(obj, float)


def allFLoatQ(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and FloatQ(i)
    return _truth


def NumberQ(obj):
    return isinstance(obj, float) or isinstance(obj, int)


def allNumberQ(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and NumberQ(i)
    return _truth


def StringQ(obj):
    return isinstance(obj, str)


def allStringQ(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and StringQ(i)
    return _truth


def MemberQ(_list: list, obj):
    try:
        return obj in _list
    except TypeError:
        print("The first argument must be list and second one a possible member type.")
        print("Das erste Argument muss in der Liste stehen und das zweite muss ein möglicher Elementtyp sein.")


def allMemberQ(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and i
    return _truth


def _round(x: float):
    try:
        if x % int(x) < 0.5:
            return int(x)
        elif x % int(x) >= 0.5:
            return int(x) + 1
    except TypeError:
        _promptReal()


def EvenQ(_number):
    _number = _round(_number)
    if _number % 2 == 0:
        return True
    else:
        return False


def OddQ(_number):
    return not EvenQ(_number)