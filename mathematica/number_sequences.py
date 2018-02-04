from mathematica.calculus import *
from mathematica.list_operations import *
from mathematica.mathematical_functions import *
from mathematica.precision import *
from mathematica.q_functions import *
from mathematica.random_functions import *
from mathematica.number_sequences import *




def Fibonacci(*kwargs):
    if len(kwargs) == 1:
        _a = 1
        _b = 1
        for i in range(0, kwargs[0]):
            _b += _a
            _a = _b
            return [_a, _b]

    elif len(kwargs) == 2:
        pass


def Tribonacci(*kwargs):
    if len(kwargs) == 1:
        pass
    elif len(kwargs) == 2:
        pass