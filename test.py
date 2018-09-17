from mathematica.load_all_functions import *

# for i in Range(0, Pi(200), 0.1):
#    print([Sin(i), Cos(i), Tan(i), Sec(i), Csc(i), Cot(i)])

import csv
import time

with open('text.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)
        for element in row:
            print(element)

for x in range(0, 5):
    b = "Loading" + "." * x + "\r"
    print(b)
    time.sleep(0.2)
