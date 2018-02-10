from mathematica.load_all_functions import *


def ListQ(obj):
    return isinstance(obj, list) or isinstance(obj, range)


def TupleQ(obj):
    return isinstance(obj, tuple)


def IntegerQ(obj):
    return isinstance(obj, int)


def FloatQ(obj):
    return isinstance(obj, float)


def NumberQ(obj):
    return isinstance(obj, float) or isinstance(obj, int)


def MemberQ(_list: list, obj):
    try:
        return obj in _list
    except TypeError:
        print("The first argument must be list and second one a possible member type.")
        print("Das erste Argument muss in der Liste stehen und das zweite muss ein möglicher Elementtyp sein.")