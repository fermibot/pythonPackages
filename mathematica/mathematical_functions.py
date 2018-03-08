from .precision import *


def Gamma(x):
    return x


def Sin(x: float):
    _sin = 0
    for i in range(50):
        _sin += (((-1)**i) * (x**((2 * i) + 1)) / (Factorial((2 * i) + 1)))
    return _sin


def Cos(x: float):
    _cos = 0
    for i in range(50):
        _cos += (((-1)**i) * (x**(2 * i)) / (Factorial(2 * i)))
    return _cos


def Tan(x: float):
    return Sin(x) / Cos(x)


def Sec(x):
    return 1 / Cos(x)


def Csc(x):
    return 1 / Sin(x)


def Cot(x):
    return Cos(x) / Sin(x)


def ArcSin(x: float):
    _arcsin = []
    for i in range(50):
        _arcsin += ((Factorial(2 * i)) * (x**((2 * i) + 1)) / ((4**i) * ((Factorial(i))**2) * (2 * i + 1)))


def ArcCos(x):
    return x


def ArcTan(x: float):
    _arctan = []
    for i in range(50):
        _arctan += (((-1)**i) * (x**(2 * i + 1)) / (2 * i + 1))
    return _arctan


def Erf(x):
    _erf = 0
    if x == 0:
        return _erf
    elif x != 0:
        _e = E()
        _pi = Pi()
        for i in Range(0, x, 0.001):
            _erf += (_e ** (- (i ** 2))) * 0.001
        return 2 * _erf / Sqrt(_pi)


def LogE(_x, _n=E()):
    _log = 0
    for i in Range(1, _x, 0.001):
        _log += 0.001 * 1 / i
    return _log


def Log10(_x):
    return LogE(_x) / LogE(10)


def Log(_x, _base):
    return LogE(_x) / LogE(_base)
