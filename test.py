from mathematica.load_all_functions import *


boxMatrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(boxMatrix)
boxMatrix[1][1] = 'a'
print(boxMatrix)


l = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
l[0][1] = "spam"
print(l)


print(BoxMatrix([2, 2, 2]))