import os
import json
from mathematica.databaseLink import SQLExecute, OpenSQLConnection
import sys
import time
from datetime import datetime
import contextlib

startTime = time.time()

directory = 'C:\\Users\\Alcatraz\\Downloads\\MyFitbitData\\AshwiniKumarKounduri\\user-site-export'
_sqlConnection = OpenSQLConnection('D:\\Programming\\_databases\\fitbitData.db')
_sqlCursor = _sqlConnection.cursor()


def timeDelta(_startTime):
    return time.strftime("%H:%M:%S", time.gmtime(time.time() - _startTime))


def heartRateExtractor(data: dict):
    return [data['dateTime'], data['value']['bpm'], data['value']['confidence']]


def altitudeExtractor(data: dict):
    return [data['dateTime'], data['value']]


def distanceExtractor(data: dict):
    return [data['dateTime'], data['value']]


class altitudeClass:
    def tableCheck(self, _dateMin, _dateMax):
        return "SELECT * FROM biometricsAltitude WHERE dateTimeID IN (\'" + _dateMin + "\', \'" + _dateMax + "\')"

    def recordCheck(self, data: dict):
        return "SELECT * FROM biometricsAltitude WHERE dateTimeID = \'" + data['dateTime'] + "\'"

    def inserter(self, data: dict):
        return "INSERT INTO biometricsAltitude VALUES ('" + data['dateTime'] + "', " + str(data['value']) + ")"


class distanceClass:
    def tableCheck(self, _dateMin, _dateMax):
        return "SELECT * FROM biometricsDistance WHERE dateTimeID IN (\'" + _dateMin + "\', \'" + _dateMax + "\')"

    def recordCheck(self, data: dict):
        return "SELECT * FROM biometricsDistance WHERE dateTimeID = \'" + data['dateTime'] + "\'"

    def inserter(self, data: dict):
        return "INSERT INTO biometricsDistance VALUES ('" + data['dateTime'] + "', " + str(data['value']) + ")"


class heartRateClass:
    def inserter(self, data: dict):
        _rec = heartRateExtractor(data)
        return "INSERT INTO biometricsHeartRate VALUES ('" + _rec[0] + "', " + str(_rec[1]) + ", " + str(_rec[2]) + ")"

    def tableCheck(self, _dateMin, _dateMax):
        return "SELECT * FROM biometricsHeartRate WHERE dateTimeID IN (\'" + _dateMin + "\', \'" + _dateMax + "\')"

    def recordCheck(self, data: dict):
        return "SELECT * FROM biometricsHeartRate WHERE dateTimeID = \'" + data['dateTime'] + "\'"


heartRate = heartRateClass()
altitude = altitudeClass()
distance = distanceClass()

mD = {'m0': 'TimeElapsed', 'm1': 'Processing file#', 'm2': 'Processing line number',
      'm3': 'record not found in the database, now inserting',
      'm4': 'suspicious record found, ',
      'm5': 'record found in the database, moving on',
      'm6': 'printing info to a logfile',
      'm7': 'Duplicate records found',
      'm8': 'This file has already been processed, moving on'
      }

_fCt = 1

metricType = {'altitude-': 9, 'heart_rate-': 11}

with open(f"D:\Programming\_databases\{'altitude'}.txt", 'w+') as altitudeLogFile, \
        open(f"D:\Programming\_databases\{'heart_rate'}.txt", 'w+') as heart_rateLogFile, \
        open(f"D:\Programming\_databases\{'distance'}.txt", 'w+') as distanceLogFile:
    for path, item, files in os.walk(directory):
        for file in files:
            if file[:9] == 'distance-':
                with open(path + '\\' + file) as inJsonFile:
                    inJsonData = json.load(inJsonFile)
                    [_dtMin, _dtMax] = [inJsonData[0]['dateTime'], inJsonData[-1]['dateTime']]
                    _timeDelta = timeDelta(startTime)
                    _tableCheck = _sqlConnection.execute(distance.tableCheck(_dtMin, _dtMax)).fetchall()
                    if len(_tableCheck) == 2:
                        sys.stdout.write(f"\r{_timeDelta}::FileCount {_fCt}::{mD['m8']}::{file}")
                        time.sleep(0.01)
                    if len(_tableCheck) < 2:
                        _rCt = 0
                        for record in inJsonData:
                            line = distanceExtractor(record)
                            _sqlResults = _sqlConnection.execute(distance.recordCheck(record)).fetchall()
                            _messagePrefix = f"{mD['m0']} {_timeDelta}::FileCount {_fCt}::{mD['m2']} {_rCt}"
                            if len(_sqlResults) == 0:
                                sys.stdout.write(f"\r{_messagePrefix}::{mD['m3']}")
                                _insertQuery = distance.inserter(record)
                                _sqlConnection.cursor().execute(_insertQuery)
                                _sqlConnection.commit()
                            elif len(_sqlResults) == 1:
                                sys.stdout.write(f"\r{_messagePrefix}::{mD['m5']}")
                            elif len(_sqlResults) > 1:
                                sys.stdout.write(f"\r{_messagePrefix}::{mD['m4']}")
                                distanceLogFile.write(f"{mD['m4']}:: {line[0]}.")
                            _rCt += 1
                        inJsonFile.close()
                    if len(_tableCheck) > 2:
                        sys.stdout.write(f"\rSeems like there is an issue with this file. {mD['m6']}")
                        distanceLogFile.write(f"{mD['m7']}::{file}")
                _fCt += 1
            if False:
                if file[:9] == 'altitude-':
                    with open(path + '\\' + file) as inJsonFile:
                        inJsonData = json.load(inJsonFile)
                        [_dtMin, _dtMax] = [inJsonData[0]['dateTime'], inJsonData[-1]['dateTime']]
                        _timeDelta = timeDelta(startTime)
                        _tableCheck = _sqlConnection.execute(altitude.tableCheck(_dtMin, _dtMax)).fetchall()
                        if len(_tableCheck) == 2:
                            sys.stdout.write(f"\r{_timeDelta}::FileCount {_fCt}::{mD['m8']}::{file}")
                            time.sleep(0.01)
                        if len(_tableCheck) < 2:
                            _rCt = 0
                            for record in inJsonData:
                                line = altitudeExtractor(record)
                                _sqlResults = _sqlConnection.execute(altitude.recordCheck(record)).fetchall()
                                _messagePrefix = f"{mD['m0']} {_timeDelta}::FileCount {_fCt}::{mD['m2']} {_rCt}"
                                if len(_sqlResults) == 0:
                                    sys.stdout.write(f"\r{_messagePrefix}::{mD['m3']}")
                                    _insertQuery = altitude.inserter(record)
                                    _sqlConnection.cursor().execute(_insertQuery)
                                    _sqlConnection.commit()
                                elif len(_sqlResults) == 1:
                                    sys.stdout.write(f"\r{_messagePrefix}::{mD['m5']}")
                                elif len(_sqlResults) > 1:
                                    sys.stdout.write(f"\r{_messagePrefix}::{mD['m4']}")
                                    altitudeLogFile.write(f"{mD['m4']}:: {line[0]}.")
                                _rCt += 1
                            inJsonFile.close()
                        if len(_tableCheck) > 2:
                            sys.stdout.write(f"\rSeems like there is an issue with this file. {mD['m6']}")
                            altitudeLogFile.write(f"{mD['m7']}::{file}")
                    _fCt += 1

                if file[:11] == 'heart_rate-':
                    with open(path + '\\' + file) as inJsonFile:
                        inJsonData = json.load(inJsonFile)
                        [_dtMin, _dtMax] = [inJsonData[0]['dateTime'], inJsonData[-1]['dateTime']]
                        _timeDelta = timeDelta(startTime)
                        _tableCheck = _sqlConnection.execute(heartRate.tableCheck(_dtMin, _dtMax)).fetchall()
                        if len(_tableCheck) == 2:
                            sys.stdout.write(f"\r{_timeDelta}::FileCount {_fCt}::{mD['m8']}::{file}")
                            time.sleep(0.01)
                        if len(_tableCheck) < 2:
                            _rCt = 0
                            for record in inJsonData:
                                line = heartRateExtractor(record)
                                _sqlResults = _sqlConnection.execute(heartRate.recordCheck(record)).fetchall()
                                _messagePrefix = f"{mD['m0']} {_timeDelta}::FileCount {_fCt}::{mD['m2']} {_rCt}"
                                if len(_sqlResults) == 0:
                                    sys.stdout.write(f"\r{_messagePrefix}::{mD['m3']}")
                                    _sqlConnection.cursor().execute(heartRate.inserter(record))
                                    _sqlConnection.commit()
                                elif len(_sqlResults) == 1:
                                    sys.stdout.write(f"\r{_messagePrefix}::{mD['m5']}")
                                elif len(_sqlResults) > 1:
                                    sys.stdout.write(f"\r{_messagePrefix}::{mD['m4']}")
                                    heart_rateLogFile.write(f"{mD['m4']}:: {line[0]}.")
                                _rCt += 1
                            inJsonFile.close()
                        if len(_tableCheck) > 2:
                            sys.stdout.write(f"\rSeems like there is an issue with this file. {mD['m6']}")
                            heart_rateLogFile.write(f"{mD['m7']}::{file}")
                    _fCt += 1
