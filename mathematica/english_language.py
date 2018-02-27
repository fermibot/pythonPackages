from .q_functions import *


# String Operations

def StringJoin(*args):
    def _subStringJoin(obj):
        if not ListQ(obj):
            return str(obj)
        elif ListQ(obj):
            _stringList = ""
            for i in obj:
                _stringList += str(i)
            return _stringList
    if len(args) == 1:
        return _subStringJoin(args[0])
    elif len(args) > 1:
        _stringJoin = []
        for i in args:
             _stringJoin.append(_subStringJoin(i))
        return _stringJoin


def ToString(*args):
    def _subToString(obj):
        if not ListQ(obj):
            return str(obj)
        elif ListQ(obj):
            _stringList = []
            for i in obj:
                _stringList.append(str(i))
            return _stringList
    if len(args) == 1:
        return _subToString(args[0])
    elif len(args) > 1:
        _toString = []
        for i in args:
            _toString.append(_subToString(i))
        return _toString


def ToUpperCase(*args):
    if (len(args) == 1) and StringQ(args[0]):
        (args[0]).upper()
    elif len(args) > 1:
        _toUpperCase = []
        for i in args:
            _toUpperCase.append(i.upper())
        return _toUpperCase


def ToLowerCase(*args):
    if (len(args) == 1) and StringQ(args[0]):
        return args[0].lower()
    elif len(args) > 1:
        _toLowerCase = []
        for i in args:
            _toLowerCase.append(i.lower())
        return _toLowerCase


def Alphabet():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']


def Characters(_string: str):
    _characters = []
    for i in _string:
        _characters.append(i)
    return _characters


def StringRiffle(*args):
    if len(args) == 1 and ListQ(args):
        _stringRiffle = ""
        for i in args[0]:
            _stringRiffle += ToString(i)
            _stringRiffle += ""
        return _stringRiffle

