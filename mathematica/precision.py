from mathematica.calculus import *
from mathematica.list_operations import *
from mathematica.mathematical_functions import *
from mathematica.precision import *
from mathematica.q_functions import *
from mathematica.random_functions import *

Pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132


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

