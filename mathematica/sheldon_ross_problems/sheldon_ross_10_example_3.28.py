from mathematica.random_functions import *
from mathematica.lists import *
from mathematica.monitoring import *
from mathematica.sheldon_ross_problems.sheldon_ross_utilities import *
import csv

unknownPath = open('folderPath.txt').readlines()[0]
chapterName = 'sheldon_ross_chapter_03'
problemName = 'sheldon_ross_example_3.28'

__fileName = ConstructFileName([unknownPath, chapterName, problemName, problemName], '_1_through_100_.csv')
TimeTagMessage('Opening file ' + __fileName)
__file = open(__fileName,'w')
TimeTagMessage('Opening writer object')
__writer = writer = csv.writer(__file, delimiter=',')


_x = Range(1, 10)
for __x in _x:
    __xList = []
    for i in range(100):
        _randomList = [RandomReal()]
        _randomElement = RandomReal()
        while Total(_randomList) < __x:
            _randomList.append(_randomElement)
        __xList.append(_randomList.__len__())
    TimeTagMessage('Writing row ' + str(__x) + ' the file')
    writer.writerow(__xList)


TimeTagMessage('Closing the file ' + __fileName)
__file.close()