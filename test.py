from mathematica.load_all_functions import *

# print(PadRight(Range(10), 20))
# print(PadRight(Range(10), 20, "x"))
# print(PadRight(Range(10), 20, ["x", "y"]))
# print(PadRight(Range(10), 11, ["x", "y"]))
# print(PadRight(Range(10), 20, "y", 4))
# print(PadRight(Range(10), 2, "y", 3))
# print(PadRight([Range(25), Range(2), Range(6), Range(11)]))
#
# print(PadLeft(Range(10), 2))
# print(PadLeft(Range(10), 11, 'c'))
# print(PadLeft(Range(10), 20, ['a', 'b', 'c']))
# print(PadLeft([Range(9), Range(1), Range(3),Range(9), Range(5)]))

# TODO: incorporate integer conversion here.
# Print(ArrayReshape(Range(96), [1, 3, 4, 4]))

#
# _centerArray = [[[0, 0, 0,], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
# exec('_centerArray[1][1][1] = 2')
# print(_centerArray)


# for i in BoxMatrix(2, 4): print(i)

print(BoxMatrix(ConstantArray(1, 3)))

for i in Range(0, 5):
    _sublist = []
    for j in Range(0, 5):
        _sublist.append(KroneckerDelta(i, j))
    print(_sublist)

print(KroneckerDelta(2, 2))