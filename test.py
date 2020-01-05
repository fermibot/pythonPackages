def factorial(x: int):
    _factorial = 1
    for i in range(1, x + 1):
        _factorial *= i
    return _factorial


def sine_cos(x, one_or_zero: 1, precision: 50):
    _sine_cos = 0
    for i in range(0, precision):
        exp_fact = 2 * i + one_or_zero
        _sine_cos += ((-1) ** i) * (x ** exp_fact) / factorial(exp_fact)
    return _sine_cos


def sin(x, precision: 50):
    return sine_cos(x, one_or_zero=1, precision=precision)


def cos(x, precision: 50):
    return sine_cos(x, one_or_zero=0, precision=precision)


if __name__ == '__main__':
    for i in range(50):
        print([cos(10, precision=i), sin(10, precision=i)])
