from mathematica.string_operations import StringDelete
from mathematica.q_functions import StringQ
import os, fnmatch


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


_directory = 'D:\Mir Book Processing'
_dataGrid = []
books = find('*', _directory)
print('The number of books i found is ' + books.__len__().__str__() + "\n")
for i in books:
   _dataGrid.append(StringDelete(i, [_directory, '\\']).split(' - '))

print(_dataGrid)