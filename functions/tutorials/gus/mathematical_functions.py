def tribonacci(n: int):
    seed_list = [0, 1, 1]
    if n <= 3:
        return seed_list[n - 1]
    if n > 3:
        for i in range(n - 3):
            new_tribonacci = sum(seed_list[-3:])
            seed_list.append(new_tribonacci)
            seed_list = seed_list[-3:]
        return seed_list[-1]


def fibonacci(n: int):
    seed_list = [1, 1]
    if n <= 2:
        return seed_list[n - 1]
    if n > 2:
        for i in range(n - 2):
            new_tribonacci = sum(seed_list[-2:])
            seed_list.append(new_tribonacci)
            seed_list = seed_list[-2:]
        return seed_list[-1]


def figurate_number(sides: int, n: int):
    offset = sides - 2
    figurate_number_internal = 0
    for i in range(0, n):
        figurate_number_internal += 1 + (offset * i)
    return figurate_number_internal


def square_root(number:int):


if __name__ == '__main__':
    for i in range(0, 20):
        print(f"Pentagonal_Number {i}::{figurate_number(5,i)}")
