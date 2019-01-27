from mathematica.string_operations import StringDelete
from mathematica.databaseLink import SQLExecute, OpenSQLConnection
from mathematica.lists import Last, Riffle, Rest
from mathematica.matrices_and_arrays import ConstantArray
from mathematica.string_operations import StringJoin
from mathematica.monitoring import TimeTagMessage
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
for i in books:
    i = StringDelete(i, [_directory, '\\', '.pdf', '.djvu']).split(' - ')
    _booksHave.append(i)
print(_booksHave)

_sqlConnection = OpenSQLConnection('D:\Programming\python\PyCharm\mathematicaPython\collections.db')


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


_updateDatabasesQ = False

if True:
    for book in _booksHave:
        book = book[0]
        _results = SQLExecute(_sqlConnection,
                              "SELECT * FROM books WHERE bookName = '" + book + "'").fetchall()
        if _results.__len__() == 0:
            _id = SQLExecute(_sqlConnection, "SELECT Max(bookID) + 1 FROM books").fetchall()[0][0]
            TimeTagMessage(" | " + book + " | Book not found in the table. Inserting into Authors")
            _sqlQuery = "INSERT INTO books (bookID, bookName, series) VALUES (" + str(_id) + ", '" + \
                        book + "', Null)"
            if _updateDatabasesQ:
                _sqlConnection.cursor().execute(_sqlQuery)
                _sqlConnection.commit()
            elif not _updateDatabasesQ:
                print(_sqlQuery + "\n")
        else:
            TimeTagMessage(" | " + book + " | Book already exists in the table. Moving on ;)")

if True:
    for authorList in _booksHave:
        authorList = Rest(authorList)
        for author in authorList:
            _nameExtract = nameExtract(author)
            _results = SQLExecute(_sqlConnection,
                                  "SELECT * FROM authors WHERE firstName = '" +
                                  _nameExtract[0] + "' AND lastName = '" + _nameExtract[1] + "'").fetchall()
            if _results.__len__() == 0:
                _id = SQLExecute(_sqlConnection, "SELECT Max(authorID) + 1 FROM authors").fetchall()[0][0]
                TimeTagMessage(" | " + author + " | Author not found in the table. Inserting into Authors")
                _sqlQuery = "INSERT INTO authors (authorID, firstName, lastName) VALUES (" + str(_id) + ", '" + \
                            _nameExtract[0] + "', '" + _nameExtract[1] + "')"
                if _updateDatabasesQ:
                    _sqlConnection.cursor().execute(_sqlQuery)
                    _sqlConnection.commit()
                elif not _updateDatabasesQ:
                    print(_sqlQuery + "\n")
            else:
                TimeTagMessage(" | " + author + " | Author already exists in the table. Moving on ;)")
