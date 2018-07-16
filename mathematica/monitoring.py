import datetime

def TimeTagMessage(string:str):
    print(datetime.datetime.utcnow().__str__() + " " + string)