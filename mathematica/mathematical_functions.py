
def Gamma(x):
    pass


def Factorial(x):
    if x == 0:
        return 1
    if (not isinstance(x, int)) or (x < 1):
            return "Non integer functionality not yet included"
    elif (isinstance(x, int)) and (x >= 1):
        _fact = 1
        for i in range(1, x + 1):
            _fact = _fact * i
        return _fact


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


def Tan(x:float):
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
    pass


def ArcTan(x: float):
    _arctan = []
    for i in range(50):
        _arctan += (((-1)**i) * (x**(2 * i + 1)) / (2 * i + 1))
    return _arctan