import os
import json
from mathematica.databaseLink import OpenSQLConnection
import sys
import time

startTime = time.time()

directory = 'C:\\Users\\Alcatraz\\Downloads\\MyFitbitData\\AshwiniKumarKounduri\\user-site-export'
_sqlConnection = OpenSQLConnection('D:\\Programming\\_databases\\fitbitData.db')
_sqlCursor = _sqlConnection.cursor()


def _dateValueExtractor(data: dict) -> list:
    return [data['dateTime'], data['value']]


def timeDelta(_startTime):
    return time.strftime("%H:%M:%S", time.gmtime(time.time() - _startTime))


def altitudeExtractor(data: dict):
    return _dateValueExtractor(data)


def distanceExtractor(data: dict):
    return _dateValueExtractor(data)


def caloriesExtractor(data: dict):
    return _dateValueExtractor(data)


def stepsExtractor(data: dict):
    return _dateValueExtractor(data)


def laMinutesExtractor(data: dict):
    return _dateValueExtractor(data)


def mAMinutesExtractor(data: dict):
    return _dateValueExtractor(data)


def sMinutesExtractor(data: dict):
    return _dateValueExtractor(data)


def vAMinutesExtractor(data: dict):
    return _dateValueExtractor(data)


def heartRateExtractor(data: dict):
    return [data['dateTime'], data['value']['bpm'], data['value']['confidence']]


class altitudeClass:
    @staticmethod
    def tableCheck(_dateMin, _dateMax):
        return "SELECT * FROM biometricsAltitude WHERE dateTimeID IN (\'" + _dateMin + "\', \'" + _dateMax + "\')"

    @staticmethod
    def recordCheck(data: dict):
        return "SELECT * FROM biometricsAltitude WHERE dateTimeID = \'" + data['dateTime'] + "\'"

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO biometricsAltitude VALUES ('" + data['dateTime'] + "', " + str(data['value']) + ")"


class caloriesClass:
    @staticmethod
    def tableCheck(_dateMin, _dateMax):
        return "SELECT * FROM biometricsCalories WHERE dateTimeID IN (\'" + _dateMin + "\', \'" + _dateMax + "\')"

    @staticmethod
    def recordCheck(data: dict):
        return "SELECT * FROM biometricsCalories WHERE dateTimeID = \'" + data['dateTime'] + "\'"

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO biometricsCalories VALUES ('" + data['dateTime'] + "', " + str(data['value']) + ")"


class distanceClass:
    @staticmethod
    def tableCheck(_dateMin, _dateMax):
        return "SELECT * FROM biometricsDistance WHERE dateTimeID IN (\'" + _dateMin + "\', \'" + _dateMax + "\')"

    @staticmethod
    def recordCheck(data: dict):
        return "SELECT * FROM biometricsDistance WHERE dateTimeID = \'" + data['dateTime'] + "\'"

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO biometricsDistance VALUES ('" + data['dateTime'] + "', " + str(data['value']) + ")"


class heartRateClass:
    @staticmethod
    def inserter(data: dict):
        _rec = heartRateExtractor(data)
        return "INSERT INTO biometricsHeartRate VALUES ('" + _rec[0] + "', " + str(_rec[1]) + ", " + str(_rec[2]) + ")"

    @staticmethod
    def tableCheck(_dateMin, _dateMax):
        return "SELECT * FROM biometricsHeartRate WHERE dateTimeID IN (\'" + _dateMin + "\', \'" + _dateMax + "\')"

    @staticmethod
    def recordCheck(data: dict):
        return "SELECT * FROM biometricsHeartRate WHERE dateTimeID = \'" + data['dateTime'] + "\'"


class stepsClass:
    @staticmethod
    def tableCheck(_dateMin, _dateMax):
        return "SELECT * FROM steps WHERE dateTimeID IN (\'" + _dateMin + "\', \'" + _dateMax + "\')"

    @staticmethod
    def recordCheck(data: dict):
        return "SELECT * FROM steps WHERE dateTimeID = \'" + data['dateTime'] + "\'"

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO steps VALUES ('" + data['dateTime'] + "', " + str(data['value']) + ")"


class lAMinutesClass:
    @staticmethod
    def tableCheck(_dateMin, _dateMax):
        return "SELECT * FROM lightlyActiveMinutes WHERE dateTimeID IN (\'" + _dateMin + "\', \'" + _dateMax + "\')"

    @staticmethod
    def recordCheck(data: dict):
        return "SELECT * FROM lightlyActiveMinutes WHERE dateTimeID = \'" + data['dateTime'] + "\'"

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO lightlyActiveMinutes VALUES ('" + data['dateTime'] + "', " + str(data['value']) + ")"


class mAMinutesClass:
    @staticmethod
    def tableCheck(_dateMin, _dateMax):
        return "SELECT * FROM moderatelyActiveMinutes WHERE dateTimeID IN (\'" + _dateMin + "\', \'" + _dateMax + "\')"

    @staticmethod
    def recordCheck(data: dict):
        return "SELECT * FROM moderatelyActiveMinutes WHERE dateTimeID = \'" + data['dateTime'] + "\'"

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO moderatelyActiveMinutes VALUES ('" + data['dateTime'] + "', " + str(data['value']) + ")"


class sMinutesClass:
    @staticmethod
    def tableCheck(_dateMin, _dateMax):
        return "SELECT * FROM sedentaryMinutes WHERE dateTimeID IN (\'" + _dateMin + "\', \'" + _dateMax + "\')"

    @staticmethod
    def recordCheck(data: dict):
        return "SELECT * FROM sedentaryMinutes WHERE dateTimeID = \'" + data['dateTime'] + "\'"

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO sedentaryMinutes VALUES ('" + data['dateTime'] + "', " + str(data['value']) + ")"


class vAMinutesClass:
    @staticmethod
    def tableCheck(_dateMin, _dateMax):
        return "SELECT * FROM veryActiveMinutes WHERE dateTimeID IN (\'" + _dateMin + "\', \'" + _dateMax + "\')"

    @staticmethod
    def recordCheck(data: dict):
        return "SELECT * FROM veryActiveMinutes WHERE dateTimeID = \'" + data['dateTime'] + "\'"

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO veryActiveMinutes VALUES ('" + data['dateTime'] + "', " + str(data['value']) + ")"


def databaseRecorder(fileName, _inJsonData, _class, _extractFunction, _logFile):
    [_dtMin, _dtMax] = [_inJsonData[0]['dateTime'], _inJsonData[-1]['dateTime']]
    _tableCheck = _sqlConnection.execute(_class.tableCheck(_dtMin, _dtMax)).fetchall()
    _timeDelta = timeDelta(startTime)
    if len(_tableCheck) == 2:
        sys.stdout.write(f"\r{_timeDelta}::FileCount {_fileTrack}::{mD['m8']}::{fileName}")
        time.sleep(0)
    if len(_tableCheck) < 2:
        _rowTrack = 0
        for record in _inJsonData:
            line = _extractFunction(record)
            _timeDelta = timeDelta(startTime)
            _sqlResults = _sqlConnection.execute(_class.recordCheck(record)).fetchall()
            _messagePrefix = f"{mD['m0']} {_timeDelta}::FileCount {_fileTrack}::{mD['m2']} {_rowTrack}"
            if len(_sqlResults) == 0:
                sys.stdout.write(f"\r{_messagePrefix}::{mD['m3']}::{fileName}")
                _sqlConnection.cursor().execute(_class.inserter(record))
                _sqlConnection.commit()
            elif len(_sqlResults) == 1:
                sys.stdout.write(f"\r{_messagePrefix}::{mD['m5']}::file {fileName}")
            elif len(_sqlResults) > 1:
                sys.stdout.write(f"\r{_messagePrefix}::{mD['m4']}")
                _logFile.write(f"{mD['m4']}:: {line[0]}.")
            _rowTrack += 1
        inJsonFile.close()
    if len(_tableCheck) > 2:
        sys.stdout.write(f"\rSeems like there is an issue with this file. {mD['m6']}")
        _logFile.write(f"{mD['m7']}::{fileName}")


mD = {'m0': 'TimeElapsed', 'm1': 'Processing file#', 'm2': 'Processing line number',
      'm3': 'record not found in the database, now inserting',
      'm4': 'suspicious record found, ',
      'm5': 'record found in the database, moving on',
      'm6': 'printing info to a logfile',
      'm7': 'Duplicate records found',
      'm8': 'This file has already been processed, moving on'
      }

_fileTrack = 1

metricType = {'altitude-': 9, 'calories-': 9, 'distance-': 9, 'heart_rate-': 11}
exportDirectory = "D:\\Programming\\_databases\\"

with open(f"{exportDirectory}{'altitude'}.txt", 'w+') as altitudeLF, \
        open(f"{exportDirectory}{'heart_rate'}.txt", 'w+') as heartRateLF, \
        open(f"{exportDirectory}{'distance'}.txt", 'w+') as distanceLF, \
        open(f"{exportDirectory}{'calories'}.txt", 'w+') as caloriesLF, \
        open(f"{exportDirectory}{'sleep'}.txt", 'w+') as stepsLF, \
        open(f"{exportDirectory}{'lightlyActiveMinutes'}.txt", 'w+') as lAMinutesLF, \
        open(f"{exportDirectory}{'moderatelyActiveMinutes'}.txt", 'w+') as mAMinutesLF, \
        open(f"{exportDirectory}{'moderatelyActiveMinutes'}.txt", 'w+') as sMinutesLF, \
        open(f"{exportDirectory}{'veryActiveMinutes'}.txt", 'w+') as vAMLogFile:
    for path, item, files in os.walk(directory):
        for file in files:
            with open(path + "\\" + file) as inJsonFile:
                if len(file) > 9 and file[-4:] == 'json':
                    inJsonData = json.load(inJsonFile)
                    if file[:9] == 'altitude-':
                        databaseRecorder(file, inJsonData, altitudeClass(), altitudeExtractor, altitudeLF)
                    elif file[:9] == 'calories-':
                        databaseRecorder(file, inJsonData, caloriesClass(), caloriesExtractor, caloriesLF)
                    elif file[:9] == 'distance-':
                        databaseRecorder(file, inJsonData, distanceClass(), distanceExtractor, distanceLF)
                    elif file[:11] == 'heart_rate-':
                        databaseRecorder(file, inJsonData, heartRateClass(), heartRateExtractor, heartRateLF)
                    elif file[:6] == 'steps-':
                        databaseRecorder(file, inJsonData, stepsClass(), stepsExtractor, stepsLF)
                    elif file[:23] == 'lightly_active_minutes-':
                        databaseRecorder(file, inJsonData, lAMinutesClass(), laMinutesExtractor, lAMinutesLF)
                    elif file[:26] == 'moderately_active_minutes-':
                        databaseRecorder(file, inJsonData, mAMinutesClass(), mAMinutesExtractor, mAMinutesLF)
                    elif file[:18] == 'sedentary_minutes-':
                        databaseRecorder(file, inJsonData, sMinutesClass(), sMinutesExtractor, sMinutesLF)
                    elif file[:20] == 'very_active_minutes-':
                        databaseRecorder(file, inJsonData, vAMinutesClass(), vAMinutesExtractor, vAMLogFile)
                    else:
                        pass
                    _fileTrack += 1
print("Database import complete")
