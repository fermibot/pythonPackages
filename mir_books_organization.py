from mathematica.string_operations import StringDelete
from mathematica.databaseLink import SQLExecute, OpenSQLConnection
from mathematica.q_functions import StringQ
import os, fnmatch
import re


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


_directory = 'D:\Mir Book Processing'
_booksHave = []
books = find('*', _directory)
# print('The number of books I found is ' + books.__len__().__str__() + "\n")
for i in books:
    i = StringDelete(i, [_directory, '\\', '.pdf', '.djvu']).split(' - ')
    _booksHave.append(i)

_sqlConnection = OpenSQLConnection('D:\Programming\python\PyCharm\mathematicaPython\collections.db')

_maxIndex = SQLExecute(_sqlConnection, "select max(authorID) from authors").fetchall()[0][0]

# for i in range(0, _booksHave.__len__()):
#     _sqlString = "INSERT INTO books VALUES (" + str(i + 1 + _maxIndex) + ", '" + _booksHave[i][0] + "', Null)"
#     _sqlString.replace("'", "\'")
#     print("Running the query " + _sqlString)
#     _sqlConnection.cursor().execute(_sqlString)
#     _sqlConnection.commit()

def nameExtract(_name:str):
    return _name

for authorList in _booksHave:
    del authorList[0]
    for author in authorList:
        _results = SQLExecute(_sqlConnection,
                          "select * from authors where firstName||lastName = '" + author + "'").fetchall()
        if _results.__len__() == 0:
            print(author + " | Author not found inserting into SQLDatabase")
            pass
        else:
            print(author + " | Author already exists")

