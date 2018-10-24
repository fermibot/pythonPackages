from sys import stdout
import sys
from mathematica.lists import EqualAll, Range
from mathematica.random_functions import RandomChoice

_steps = 5000
_subSteps = _steps // 100
_n = 10
_set = Range(_n)

for _k in range(3, 6):
    _progressPad = "_" * 106
    _file = open(
        'D:\Mathematica Files 4K\sheldon_ross\sheldon_ross_chapter_03\sheldon_ross_exercise_3.22\sheldon_ross_10_exercise_3.22_' + str(_n) + '_' + str(
            _k) + '.txt', 'w')

    print("\n\nWriting data to the file :" + _file.name)
    print(_progressPad)

    for i in range(0, _steps):
        _sample = RandomChoice(_set, _k)
        while True:
            if EqualAll(_sample[-_k:]):
                break
            else:
                _sample.append(RandomChoice(_set))
        _file.write(_sample.__str__().replace("[", "{").replace("]", "}") + '\n')
        if (i + 1) % _subSteps == 0:
            stdout.write("\r" + ("\r" + ("#" * (i // _subSteps + 1)).ljust(100)) + " " + str(
                i // _subSteps + 1) + " %")
            stdout.flush()
print("\nClosing the file: " + _file.name)
_file.close()
