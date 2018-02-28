from mathematica.load_all_functions import *

print(Append(Range(100), 20))
print(Prepend(Range(100), 20))
print(Characters('A String'))
print(StringRiffle(Characters("A String")))
print(StringRiffle(Characters("A String"), ","))
print(StringRiffle(Characters("A String"), ["(", " ", ")"]))
print(StringRiffle([Range(21, 30), Range(34, 43), Range(11, 20, 1)]))
print(StringRiffle([Range(10), Range(10), Range(10)], "\n", "\t"))

print(StringRepeat("String", 3))
print(StringRepeat("String", 20, 15))