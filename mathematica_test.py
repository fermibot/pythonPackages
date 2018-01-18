from mathematica import random_functions
from mathematica import list_operations as lo

# print()
#
# print("Random Integer ", end="")
# print(random_functions.RandomInteger(0, 200, 46))
#
# print("Uniform dist   ", end="")
# print(random_functions.UniformDistribution(0, 200, 10))
#
# print("Triang dist    ", end="")
# print(random_functions.TriangularDistribution(-1, 2, 1.5, 10))
#
# print("Beta dist      ", end="")
# print(random_functions.BetaDistribution(1, 2, 10))
#
# print("Gamma dist     ", end="")
# print(random_functions.GammaDistribution(1, 2, 10))
#
# print("LogNorm dist   ", end="")
# print(random_functions.LogNormalDistribution(1, 2, 10))
#
# print("Exp dist       ", end="")
# print(random_functions.ExponentialDistribution(1, 10))
#
# print("Norm Dist      ", end="")
# print(random_functions.NormalDistribution(0, 1, 10))
#
# print("VonMises Dist  ", end="")
# print(random_functions.VonMisesDistribution(0, 1, 10))
#
# print("Weibull Dist   ", end="")
# print(random_functions.WeibullDistribution(0.1, 1, 10))
#
# print("Rand Choice    ", end="")
# print(random_functions.RandomChoice(list(range(0, 10)), 67))
#
# print("Rand Sample    ", end="")
# print(random_functions.RandomSample(list(range(0, 53)), 53))


print(lo.Range(9.5))
print(lo.First(lo.Range(2, 3)))
print(lo.Last(lo.Range(2, 3)))
print(lo.Reverse(lo.Range(10)))