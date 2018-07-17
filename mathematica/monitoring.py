import datetime


def TimeTagMessage(string):
    print(datetime.datetime.utcnow().__str__() + " " + string)