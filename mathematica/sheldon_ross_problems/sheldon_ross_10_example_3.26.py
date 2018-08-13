from mathematica.random_functions import *
from mathematica.lists import *
from mathematica.monitoring import *
from mathematica.sheldon_ross_problems.sheldon_ross_utilities import *


# Example 3.26 At a party n men take off their hats. The hats are then mixed up
# and each man randomly selects one. We say that a match occurs if a man selects
# his own hat. What is the probability of no matches? What is the probability of
# exactly k matches?


unknownPath = open('folderPath.txt').readlines()[0]
chapterName = 'sheldon_ross_chapter_03'
problemName = 'sheldon_ross_example_3.26'

__fileName = ConstructFileName([unknownPath, chapterName, problemName, problemName], '_' + '.txt')
__file = open(__fileName, 'w')

TimeTagMessage('Opening file ' + __fileName)
TimeTagMessage('Writing into file')


_men = 1000
for i in range(100000):
    __file.write(str(ListCompare(Range(_men), RandomSample(Range(_men), _men)).count(True)) + '\n')

TimeTagMessage('Closing the file ' + __fileName)
__file.close()


def MyFunction():
    return None

