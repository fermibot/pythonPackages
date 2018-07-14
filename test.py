from mathematica.load_all_functions import *
import datetime


print("Sampling " + datetime.datetime.utcnow().__str__())
__size = 5000
__list = RandomSample(Range(1, __size), __size)
print("Quicksort Start " + datetime.datetime.utcnow().__str__())
QuickSort(__list)
print("Quicksort End   " + datetime.datetime.utcnow().__str__())
__list.sort()
print("Python Sort End " + datetime.datetime.utcnow().__str__())
