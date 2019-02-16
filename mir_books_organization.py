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


_directory = 'D:\Mir Books Processing'
_booksHave = []
books = find('*', _directory)
for data in books:
    data = StringDelete(data, [_directory, '\\', '.pdf', '.djvu']).split(' - ')
    _booksHave.append(data)
# print(_booksHave)

_sqlConnection = OpenSQLConnection('D:\Programming\_databases\collections.db')


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


print("Found a total of " + str(_booksHave.__len__()) + "\n")

for data in _booksHave:
    _book = data[0]
    _authors = Rest(data)

if True:
    _updateDatabasesQ = True

    _bookTrack01 = 1
    _bookLength = _booksHave.__len__()
    TimeTagMessage("Starting Books Upload")
    if True:
        for book in _booksHave:
            book = book[0]
            _bookSQLResults = SQLExecute(_sqlConnection,
                                  "SELECT * FROM books WHERE bookName = '" + book + "'").fetchall()
            _prefix = " | Progress " + str(_bookTrack01) + " off " + str(_bookLength)
            if _bookSQLResults.__len__() == 0:
                _bookId = SQLExecute(_sqlConnection, "SELECT Max(bookID) + 1 FROM books").fetchall()[0][0]
                TimeTagMessage(" | Progress " + str(_bookTrack01) + " off " + str(
                    _bookLength) + " | Book not found in the table. Inserting into books.\t | " + book)
                _sqlQuery = "INSERT INTO books (bookID, bookName, series) VALUES (" + str(_bookId) + ", '" + \
                            book + "', NULL)"
                if _updateDatabasesQ:
                    _sqlConnection.cursor().execute(_sqlQuery)
                    _sqlConnection.commit()
                elif not _updateDatabasesQ:
                    print(_sqlQuery + "\n")
            else:
                _bookId = _bookSQLResults[0][0]
                TimeTagMessage(_prefix + " | Book already exists in the table. Moving on.\t\t | " + book)
            _bookTrack01 += 1

    print("")
    TimeTagMessage("Starting Authors Upload")
    if True:
        _bookTrack02 = 1
        for authorList in _booksHave:
            authorList = Rest(authorList)
            _authorTrack = 1
            _authorLength = authorList.__len__()
            for _author in authorList:
                _nameExtract = nameExtract(_author)
                _authorSQLResults = SQLExecute(_sqlConnection,
                                      "SELECT * FROM authors WHERE firstName = '" +
                                               _nameExtract[0] + "' AND lastName = '" + _nameExtract[1] + "'").fetchall()
                _prefix = " | Book " + str(_bookTrack02) + " off " + str(_bookLength) + " | Author " + str(
                    _authorTrack) + " off " + str(
                    _authorLength)
                if _authorSQLResults.__len__() == 0:
                    _authorId = SQLExecute(_sqlConnection, "SELECT Max(authorID) + 1 FROM authors").fetchall()[0][0]
                    TimeTagMessage(
                        _prefix + " | Author not found in the table. Inserting into authors.\t | " + _author)
                    _sqlQuery = "INSERT INTO authors (authorID, firstName, lastName) VALUES (" + str(
                        _authorId) + ", '" + \
                                _nameExtract[0] + "', '" + _nameExtract[1] + "')"
                    if _updateDatabasesQ:
                        _sqlConnection.cursor().execute(_sqlQuery)
                        _sqlConnection.commit()
                    elif not _updateDatabasesQ:
                        print(_sqlQuery + "\n")
                else:
                    _authorId = _authorSQLResults[0][0]
                    TimeTagMessage(_prefix + " | Author already exists in the table. Moving on.\t\t | " + _author)
                _authorTrack += 1
            _bookTrack02 += 1
