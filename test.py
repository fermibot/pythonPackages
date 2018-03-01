from mathematica.load_all_functions import *


print(PadRight(Range(10), 20))
print(PadRight(Range(10), 20, "x"))
print(PadRight(Range(10), 20, "y", 4))
print(PadRight(Range(10), 20, ["x", "y"]))
