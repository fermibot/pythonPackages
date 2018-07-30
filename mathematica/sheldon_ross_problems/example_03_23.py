from mathematica.random_functions import *
from mathematica.lists import *

randomSample = RandomChoice(Range(10), 10)
lastExcluded = randomSample[3]
foundLargest = 0
i = 4
for i in range(4, len(randomSample)):
    while