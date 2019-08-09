def IntegerDigits(integer):
    integer_digits = []
    power = 0
    divisor = 10 ** power
    while integer // divisor > 0:
        integer_digits = [integer // 10 ** power % 10] + integer_digits
        divisor = 10 ** power
        power += 1
    return integer_digits[1:]


if __name__ == '__main__':
    print(IntegerDigits(123456789))
