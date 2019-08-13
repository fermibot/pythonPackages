def Tribonacci(n: int):
    seedList = [0, 1, 1]
    if n <= 3:
        return seedList[n - 1]
    if n > 3:
        for i in range(n - 3):
            newTribonacci = sum(seedList[-3:])
            seedList.append(newTribonacci)
            seedList = seedList[-3:]
        return seedList[-1]


def Fibonacci(n: int):
    seedList = [1, 1]
    if n <= 2:
        return seedList[n - 1]
    if n > 2:
        for i in range(n - 2):
            newTribonacci = sum(seedList[-2:])
            seedList.append(newTribonacci)
            seedList = seedList[-2:]
        return seedList[-1]


def TriangularNumber(n: int) -> int:
    return int((1 / 2 * n ** 2) + (3 / 2 * n) + 1)


def SquareNumber(n: int) -> int:
    return int((n ** 2) + (2 * n) + 1)


if __name__ == '__main__':
    for i in range(0, 20):
        print(f"Square {i} {SquareNumber(i)}")
