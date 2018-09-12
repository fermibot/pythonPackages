from mathematica.load_all_functions import *

for i in Range(0, Pi(200), 0.1):
    print([Sin(i), Cos(i), Tan(i), Sec(i), Csc(i), Cot(i)])