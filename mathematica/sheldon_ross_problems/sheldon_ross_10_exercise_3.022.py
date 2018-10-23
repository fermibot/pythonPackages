from sys import stdout
from mathematica.lists import EqualAll, Range
from mathematica.random_functions import RandomChoice

print("Opening the text file")
_file = open(
    'D:\Mathematica Files 4K\sheldon_ross\sheldon_ross_chapter_03\sheldon_ross_exercise_3.22\sheldon_ross_10_exercise_3.22.txt',
    'w')

print("Initializing the loop and writing to the text file")

print("_" * 106)

_steps = 1000
_subSteps = _steps // 100
for i in range(0, _steps):
    _set = Range(5)
    _k = 3
    _sample = RandomChoice(_set, _k)
    while True:
        if EqualAll(_sample[-3:]):
            break
        else:
            _sample.append(RandomChoice(_set))
    _file.write(_sample.__str__().replace("[", "{").replace("]", "}") + '\n')
    if (i + 1) % _subSteps == 0:
        stdout.write("\r" + ("\r" + ("#" * (i // _subSteps + 1)).ljust(100)) + " " + str(i // _subSteps + 1) + " %")
        stdout.flush()

