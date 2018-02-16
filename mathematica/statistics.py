from mathematica.precision import *

def Total(_list: list):
    _total = float(0)
    for i in _list:
        _total += i
    return _total


def Mean(_list: list):
    return Total(_list) / len(_list)


def SampleMean(_sample: list):
    return Total(_sample) / (len(_sample) - 1)


def Variance(_sample: list):
    _mean = Mean(_sample)
    _squaredErrors = []
    for i in _sample:
        _squaredErrors.append((_mean - i) ** 2)
    return SampleMean(_squaredErrors)


def StandardDeviation(_sample: list):
    _mean = Mean(_sample)
    _squaredErrors = []
    for i in _sample:
        _squaredErrors.append((_mean - i) ** 2)
    return SampleMean(_squaredErrors) ** 0.5


def Skewness(_sample: list):
    _mean = Mean(_sample)
    _cubedErrors = []
    for i in _sample:
        _cubedErrors.append((_mean - i) ** 3)
    return SampleMean(_cubedErrors) / (Variance(_sample) ** 1.5)


def Kurtosis(_sample: list):
    _mean = Mean(_sample)
    _kurtedErrors = []
    for i in _sample:
        _kurtedErrors.append((_mean - i) ** 4)
    return SampleMean(_kurtedErrors) / (Variance(_sample) ** 2)


def NormalDistributionPDF(x, mu: float=0, sigma: float=1):
    _factor = 1 / Sqrt(2 * Pi * (sigma ** 2))
    _exponent = ((x - mu) ** 2) / (2 * (sigma ** 2))
    return _factor * (E ** (-_exponent))


