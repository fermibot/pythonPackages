from mathematica.string_operations import StringDelete
from mathematica.databaseLink import SQLExecute, OpenSQLConnection
from mathematica.lists import Last, Riffle
from mathematica.matrices_and_arrays import ConstantArray
from mathematica.string_operations import StringJoin
import os, fnmatch


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

def nameExtract(_name: str):
    if "." in _name:
        _name = _name.split('.')
        _lastName = Last(_name)
        del _name[-1]
        _name = Riffle(_name, ConstantArray(".", len(_name))) + ["."]
        _name = StringJoin(_name)
        return [_name, _lastName]
    if "." not in _name:
        return _name.split(' ')


_id = 30
for authorList in _booksHave:
    del authorList[0]
    for author in authorList:
        _results = SQLExecute(_sqlConnection,
                              "select * from authors where firstName||lastName = '" + author + "'").fetchall()
        if _results.__len__() == 0:
            _nameExtract = nameExtract(author)
            print(author + " | Author not found. Inserting into Authors")
            print("INSERT INTO authors (authorID, firstName, lastName) VALUES (" + str(_id) + ", '" + _nameExtract[
                0] + ", '" + _nameExtract[1] + "')")
            print("")
            pass
        else:
            print(author + " | Author already exists")
            print(nameExtract(author))
            print("")
