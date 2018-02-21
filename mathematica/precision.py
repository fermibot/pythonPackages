from .q_functions import *
from .base_functions import *

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



def _promptReal():
    print("Input needs to be a real number \nDie Eingabe muss eine reelle Zahl sein")


def Round(x: float):
    try:
        if x % int(x) < 0.5:
            return int(x)
        elif x % int(x) >= 0.5:
            return int(x) + 1
    except TypeError:
        _promptReal()


def Floor(x: float):
    try:
        return int(x)
    except TypeError:
        _promptReal()


def Ceiling(x: float):
    try:
        return int(x) + 1
    except TypeError:
        _promptReal()


def Abs(x: float):
    try:
        if x >= 0:
            _x = x
        elif x <=0:
            _x = -1 * x
        return _x
    except TypeError:
        _promptReal()
        # TODO: This prints a redundant none statement.


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



def Power(*kwargs):
    if NumberQ(kwargs[0]) and NumberQ(kwargs[1]):
        return kwargs[0] ** kwargs[1]
    elif NumberQ(kwargs[0]) and ListQ(kwargs[1]):
        _list = []
        for i in kwargs[1]:
            _list.append(kwargs[0] ** i)
        return _list
    elif ListQ(kwargs[0]) and NumberQ(kwargs[1]):
        _list = []
        for i in kwargs[0]:
            _list.append(i ** kwargs[1])
        return _list
    elif ListQ(kwargs[0]) and ListQ(kwargs[1]):
        if len(kwargs[0]) == len(kwargs[1]):
            _list = []
            for i in range(0, len(kwargs[0])):
                _list.append(kwargs[0][i] ** kwargs[0][i])
            return _list
        elif len(kwargs[0]) != len(kwargs[1]):
            _list = []
            for i in kwargs[0]:
                _listt = []
                for j in kwargs[1]:
                    _listt.append(i ** j)
                _list.append(_listt)
            return _list
    else:
        print("Help document")


def BaseForm(number: int, base: int):
    pass