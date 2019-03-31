import os
import json
from mathematica.databaseLink import SQLExecute, OpenSQLConnection
import sys
import time
import datetime

startTime = time.time()

directory = 'C:\\Users\\Alcatraz\\Downloads\\MyFitbitData\\AshwiniKumarKounduri\\user-site-export'
_sqlConnection = OpenSQLConnection('D:\\Programming\\_databases\\collections.db')
_sqlCursor = _sqlConnection.cursor()

_fileCount = 1

metricType = 'heart_rate-'
with open(f'D:\Programming\_databases\{metricType}.txt', 'w+') as logFile:
    for path, item, files in os.walk(directory):
        for file in files:
            if file[:11] == 'heart_rate-':
                if False:
                    with open(path + '\\' + file) as incomingJsonFile:
                        incomingJsonFileData = json.load(incomingJsonFile)
                        rowCount = 0
                        for line in incomingJsonFileData:
                            _sqlResults = _sqlConnection.execute(
                                "SELECT * FROM biometricsHeartRate WHERE dateTimeID = \'" +
                                line['dateTime'] + "\'").fetchall()
                            _timeDifference = time.strftime("%H:%M:%S", time.gmtime(time.time() - startTime))
                            _messagePrefix = f'TimeElapsed {_timeDifference}::Processing file#{_fileCount}::Processing line number {rowCount}'
                            if len(_sqlResults) == 0:
                                sys.stdout.write(
                                    f'\r{_messagePrefix}::record not found in the database, now inserting')
                                _insertQuery = "INSERT INTO biometricsHeartRate (dateTimeID, bpm, confidence) VALUES ('" + \
                                               line['dateTime'] + "', " + str(line['value']['bpm']) + ", " + \
                                               str(line['value']['confidence']) + ")"
                                _sqlConnection.cursor().execute(_insertQuery)
                                _sqlConnection.commit()
                            elif len(_sqlResults) == 1:
                                sys.stdout.write(
                                    f'\r{_messagePrefix}::record found in the database, moving on.')
                            elif len(_sqlResults) > 1:
                                sys.stdout.write(
                                    f'\r{_messagePrefix}::suspicious record found, printing data to a logfile.')
                                logFile.write('Duplicate records for the instance: ' + str(line['dateTime']))
                            rowCount += 1
                        incomingJsonFile.close()
                    _fileCount += 1
