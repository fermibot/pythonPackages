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
books = find('*', _directory)  # finds all the files that match the pattern '*'
for i in books:  # runs a loop across the list of the files found
    print(StringDelete(i, [_directory,'\\']))
    print("")
