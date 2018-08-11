from mathematica.random_functions import *
from mathematica.lists import *
from mathematica.monitoring import *
from mathematica.sheldon_ross_problems.sheldon_ross_utilities import *

unknownPath = open('folderPath.txt').readlines()[0]
chapterName = 'sheldon_ross_chapter_03'
problemName = 'sheldon_ross_example_3.25'


def bestGift():
    for variableGifts in [10, 50, 100]:
        numberOfGifts = variableGifts

        for rejInd in range(0, numberOfGifts):
            __fileName = ConstructFileName([unknownPath, chapterName, problemName, problemName], '_' + str(numberOfGifts) + '_'
                                           + str(rejInd) + '.txt')
            __file = open(__fileName, 'w')

            TimeTagMessage('Opening file ' + __fileName)
            TimeTagMessage('Writing into file')

            for r in range(0, 1000000):
                randomSample = RandomSample(Range(numberOfGifts), numberOfGifts)
                rejectedIndex = rejInd
                rejectedSequence = randomSample[0:rejectedIndex]
                unRejectedSequence = randomSample[rejectedIndex:len(randomSample)]

                accepted = None
                for i in unRejectedSequence:
                    if GreaterThanAll(i, rejectedSequence):
                        accepted = i
                        break
                __file.write(str(accepted) + '\n')

            TimeTagMessage('Closing the file ' + __fileName)
            __file.close()
            print('')


def worstGift():
    for variableGifts in [10, 50, 100]:
        numberOfGifts = variableGifts

        for rejInd in range(0, numberOfGifts):
            __fileName = ConstructFileName([unknownPath, chapterName, problemName, problemName],
                                           '_worst_' + str(numberOfGifts) + '_'
                                           + str(rejInd) + '.txt')
            __file = open(__fileName, 'w')

            TimeTagMessage('Opening file ' + __fileName)
            TimeTagMessage('Writing into file')

            for r in range(0, 1000000):
                randomSample = RandomSample(Range(numberOfGifts), numberOfGifts)
                rejectedIndex = rejInd
                rejectedSequence = randomSample[0:rejectedIndex]
                unRejectedSequence = randomSample[rejectedIndex:len(randomSample)]

                accepted = None
                for i in unRejectedSequence:
                    if LessThanAll(i, rejectedSequence):
                        accepted = i
                        break
                __file.write(str(accepted) + '\n')

            TimeTagMessage('Closing the file ' + __fileName)
            __file.close()
            print('')


bestGift()
worstGift()

