from sys import stdout
from mathematica.random_functions import RandomReal
import csv

_folderPath = 'D:\\Mathematica Files 4K\\sheldon_ross\\sheldon_ross_chapter_03\\sheldon_ross_exercise_3.26\\'

_probabilities = [0.2, 0.3]


def _randomChoiceCustom(_probability):
    _result = 0
    if RandomReal() <= _probability:
        _result = 1
    return _result


_csvfile = open(_folderPath + 'sheldon_ross_10_exercise_3.26.csv', 'w', newline='')
_csvWriter = csv.writer(_csvfile)

_steps = 100000
_subSteps = _steps // 100
_progressPadTop = "-" * 106
_progressPadBottom = "-" * 106

print("\n\nWriting data to the file :" + _csvfile.name)
print(_progressPadTop)
for i in range(0, _steps):
    _i = 0
    _games = []
    while True:
        _games.append(_randomChoiceCustom(_probabilities[_i % 2]))
        _i += 1
        if _games[-2:] == [1, 1]:
            break
    _csvWriter.writerow(_games)
    if (i + 1) % _subSteps == 0:
        stdout.write("\r" + ("\r" + ("#" * (i // _subSteps + 1)).ljust(100)) + " " + str(
            i // _subSteps + 1) + " %")
        stdout.flush()

print("\n" + _progressPadBottom)
print("Closing the file: " + _csvfile.name)

_csvfile.close()
