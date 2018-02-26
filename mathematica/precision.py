from .core_functions import *

Pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132
E = 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320


def Pi(precision: int=200):
    _pi = 0
    for i in range(0, precision):
        _pi += (Factorial(i) / Factorial2(2 * i + 1))
    return round(float(2 * _pi), 200)


def E(precision: int=200):
    _e = 0
    for i in range(0, precision):
        _e += (1 / Factorial(i))
    return round(float(_e), 200)



def Round(x: float):
    try:
        _x = x
        x = Abs(x)
        if x == 0:
            return 0
        elif x % int(x) < 0.5:
            return Sign(_x) * int(x)
        elif x % int(x) >= 0.5:
            return Sign(_x) * (int(x) + 1)
    except TypeError:
        promptReal()


def Clip(*args):
    if len(args) == 1:
        _x = args[0]
        if -1 < _x < 1:
            return _x
        elif _x <= -1:
            return -1
        elif _x >= 1:
            return 1
    elif len(args) == 2 and ListQ(args[1]):
        _x = args[0]
        if args[1][0] < _x < args[1][1]:
            return _x
        elif _x <= args[1][0]:
            return args[1][0]
        elif _x >= args[1][1]:
            return args[1][1]
    elif len(args) == 3 and ListQ(args[1]) and ListQ(args[2]):
        _x = args[0]
        if args[1][0] < _x < args[1][1]:
            return _x
        elif _x <= args[1][0]:
            return args[2][0]
        elif _x >= args[1][1]:
            return args[2][1]




def Floor(x: float):
    try:
        return int(x)
    except TypeError:
        promptReal()


def Ceiling(x: float):
    try:
        return int(x) + 1
    except TypeError:
        promptReal()


def Sqrt(n):
    if NumberQ(n):
        _precision = 10
        if n == 0:
            return 0
        elif n >= 1:
            _sqrt = float(1)
            i = 0
            while i <= _precision:
                j = 0
                _step = 1 / (10 ** i)
                while ((_sqrt + _step) ** 2) <= n:
                    _sqrt += 1 / (10 ** i)
                    j += 1
                i += 1
            return _sqrt
        elif 0 < n < 1:
            pass
    else:
        return "enter a real number"


def CubeRoot(n):
    if NumberQ(n):
        _precision = 10
        if n == 0:
            return 0
        elif n >= 1:
            _cubeRoot = float(1)
            i = 0
            while i <= _precision:
                j = 0
                _step = 1 / (10 ** i)
                while ((_cubeRoot + _step) ** 3) <= n:
                    _cubeRoot += 1 / (10 ** i)
                    j += 1
                i += 1
            return _cubeRoot
        elif 0 < n < 1:
            pass
    else:
        return "enter a real number"


def Surd(x, n):
    if NumberQ(x):
        _precision = 10
        if x == 0:
            return 0
        elif x >= 1:
            _surd = float(1)
            i = 0
            while i <= _precision:
                j = 0
                _step = 1 / (10 ** i)
                while ((_surd + _step) ** n) <= x:
                    _surd += 1 / (10 ** i)
                    j += 1
                i += 1
            return _surd
        elif 0 < x < 1:
            pass
    else:
        return "enter a real number"



def Power(*args):
    if NumberQ(args[0]) and NumberQ(args[1]):
        return args[0] ** args[1]
    elif NumberQ(args[0]) and ListQ(args[1]):
        _list = []
        for i in args[1]:
            _list.append(args[0] ** i)
        return _list
    elif ListQ(args[0]) and NumberQ(args[1]):
        _list = []
        for i in args[0]:
            _list.append(i ** args[1])
        return _list
    elif ListQ(args[0]) and ListQ(args[1]):
        if len(args[0]) == len(args[1]):
            _list = []
            for i in range(0, len(args[0])):
                _list.append(args[0][i] ** args[0][i])
            return _list
        elif len(args[0]) != len(args[1]):
            _list = []
            for i in args[0]:
                _listt = []
                for j in args[1]:
                    _listt.append(i ** j)
                _list.append(_listt)
            return _list
    else:
        print("Help document")


def Resacle(*args):
    def _rescaleHelp(*args):
        return (args[0] - args[1][0]) / Abs(args[1][0] - args[1][1])
    if len(args) == 2:
        _rescaleHelp(args[0], args[1])
        # TODO: need to repair this function later-on ;)

def BaseForm(number: int, base: int):
    pass