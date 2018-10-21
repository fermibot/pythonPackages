from sys import stdout
from mathematica.random_functions import RandomChoice, RandomReal
from mathematica.lists import Transpose
from mathematica.string_operations import StringPadLeft, StringPadRight

_file = open(
    'D:\Mathematica Files 4K\sheldon_ross\sheldon_ross_chapter_03\sheldon_ross_exercise_3.21\sheldon_ross_10_exercise_3.21.txt',
    'w')

for i in range(0, 1000000):
    _n, _time = 0, 0
    while True:
        _n += 1
        _rand = RandomReal()
        if 0 <= _rand < 1 / 3:
            _time += 2
            break
        elif 1 / 3 <= _rand < 2 / 3:
            _time += 3
        elif 2 / 3 <= _rand <= 1:
            _time += 5
    _file.write({_n, _time}.__str__() + '\n')
    if (i + 1) % 1000 == 0:
        # stdout.write("\rWriting line #" + str(i + 1) + " to the file.")
        stdout.write( "\r" + ("#" * (i // 10000)))
        stdout.flush()
