from mathematica.random_functions import *
# print()
# print("Random Integer ", end="")
# print(RandomInteger(0, 200, 46))
# print("Uniform dist   ", end="")
# print(UniformDistribution(0, 200, 10))
# print("Triang dist    ", end="")
# print(TriangularDistribution(-1, 2, 1.5, 10))
# print("Beta dist      ", end="")
# print(BetaDistribution(1, 2, 10))
# print("Gamma dist     ", end="")
# print(GammaDistribution(1, 2, 10))
# print("LogNorm dist   ", end="")
# print(LogNormalDistribution(1, 2, 10))
# print("Exp dist       ", end="")
# print(ExponentialDistribution(1, 10))
# print("Norm Dist      ", end="")
# print(NormalDistribution(0, 1, 10))
# print("VonMises Dist  ", end="")
# print(VonMisesDistribution(0, 1, 10))
# print("Weibull Dist   ", end="")
# print(WeibullDistribution(0.1, 1, 10))
# print("Rand Choice    ", end="")
# print(RandomChoice(list(range(0, 10)), 67))
# print("Rand Sample    ", end="")
# print(RandomSample(list(range(0, 53)), 53))


from mathematica.mathematical_functions import *
# print(Factorial(5))
# print(Factorial(3.0))
# print(Factorial(0))
# print(Sin(0))
# print(Cos(0))
# print(Tan(0))
# print(Sec(0))
# print(Csc(0.01))
# print(Cot(0.01))


from mathematica.precision import *
# print(Ceiling(1.2))
# print(Ceiling(1.66))
# print(Round(1.2))
# print(Round(1.66))
# print(Floor(1.99))
# print(Floor(1.2))


from mathematica.list_operations import *
#
# print(Range(9.5))
# print(First(Range(2, 3)))
# print(Last(Range(2, 3)))
# print(Reverse(Range(10)))
# print(Head(Range(9.5)))
# print(Tuples([1, 2, 3], 4))
# print(Transpose([[1, 2, 3], [4, 5, 6]]))
# print(Range(1, 2, 0.2))

# print(Reverse("string"))
# print(Reverse([1, 3, 4, 6]))
# print(Reverse([(1, 2), (2, 4)]))
# print(Reverse(range(0, 10)))

# print(CirclePoints(100))
# print(CirclePoints(2, 25))
# print(CirclePoints([2, Pi], 25))
# print(CirclePoints([1, 1], [2, 0], 4))
# print(Subdivide(10))
# print(Subdivide(10, 21))
# print(Subdivide(10, 20, 200))
# print(Union([1, 2, 3, 3, 3, 4, 4, 5]))
# print(Partition([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14], 7)
# print(SparseArray([[[1, 1], 2], [[2, 3], 2], [[3, 3], 5]]))
# # print(SparseArray([[1, 1], [2, 3], [2, 4]], [1, 3, 5]))
# print(PowerRange(100000000))
# print(PowerRange(1, 9462165999))
# print(PowerRange(1, 9462165999, 4))


from mathematica.number_sequences import *

for i in Power(range(2, 10), range(1, 5)):
    print(i)

