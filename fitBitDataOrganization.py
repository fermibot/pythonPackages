import os
import json
from mathematica.databaseLink import SQLExecute, OpenSQLConnection
import sys
import time
from datetime import datetime

startTime = time.time()

directory = 'C:\\Users\\Alcatraz\\Downloads\\MyFitbitData\\AshwiniKumarKounduri\\user-site-export'
_sqlConnection = OpenSQLConnection('D:\\Programming\\_databases\\collections.db')
_sqlCursor = _sqlConnection.cursor()


def heartRateInfoExtractor(data: dict):
    return [data['dateTime'], data['value']['bpm'], data['value']['confidence']]


mD = {'m0': 'TimeElapsed', 'm1': 'Processing file#', 'm2': 'Processing line number',
      'm3': 'record not found in the database, now inserting',
      'm4': 'suspicious record found, ',
      'm5': 'record found in the database, moving on',
      'm6': 'printing info to a logfile',
      'm7': 'Duplicate records found',
      'm8': 'This file has already been processed. Moving on'
      }

_fCt = 1

metricType = 'heart_rate-'
with open(f'D:\Programming\_databases\{metricType}.txt', 'w+') as logFile:
    for path, item, files in os.walk(directory):
        for file in files:
            if file[:11] == 'heart_rate-':
                with open(path + '\\' + file) as incomingJsonFile:
                    incomingJsonFileData = json.load(incomingJsonFile)
                    [_dtMin, _dtMax] = [incomingJsonFileData[0]['dateTime'], incomingJsonFileData[-1]['dateTime']]
                    _tableCheck = "SELECT * FROM biometricsHeartRate WHERE dateTimeID IN (\'" + _dtMin + "\', \'" + _dtMax + "\')"
                    _tableCheck = _sqlConnection.execute(_tableCheck).fetchall()
                    if len(_tableCheck) == 2:
                        sys.stdout.write(f"\r{mD['m8']}::{file}")
                        time.sleep(0.2)
                    if len(_tableCheck) < 2:
                        incomingJsonFileData = map(heartRateInfoExtractor, incomingJsonFileData)
                        _rCt = 0
                        for line in incomingJsonFileData:
                            _sqlResults = _sqlConnection.execute(
                                "SELECT * FROM biometricsHeartRate WHERE dateTimeID = \'" + line[0] + "\'").fetchall()
                            _timeDelta = time.strftime("%H:%M:%S", time.gmtime(time.time() - startTime))
                            _messagePrefix = f"{mD['m0']} {_timeDelta}::FileCount {_fCt}::{mD['m2']} {_rCt}"
                            if len(_sqlResults) == 0:
                                sys.stdout.write(f"\r{_messagePrefix}::{mD['m3']}")
                                _insertQuery = "INSERT INTO biometricsHeartRate VALUES ('" \
                                               + line[0] + "', " + str(line[1]) + ", " + str(line[2]) + ")"
                                _sqlConnection.cursor().execute(_insertQuery)
                                _sqlConnection.commit()
                            elif len(_sqlResults) == 1:
                                sys.stdout.write(f"\r{_messagePrefix}::.")
                            elif len(_sqlResults) > 1:
                                sys.stdout.write(f"\r{_messagePrefix}::{mD['m4']}")
                                logFile.write(f"{mD['m4']}:: {line[0]}.")
                            _rCt += 1
                        incomingJsonFile.close()
                    if len(_tableCheck) > 2:
                        sys.stdout.write(f"\rSeems like there is an issue with this file. {mD['m6']}")
                        logFile.write(f"{mD['m7']}::{file}")
                _fCt += 1
                if _fCt > 16:
                    break
