import glob
import csv
import sys
import re


def yearReplace(dateString: str) -> str:
    if dateString.split('\t')[0].__len__() != 10:
        time = re.findall('..:..:..', dateString)[0]
        return dateString.replace('/18 ', '/2018 ').replace('/19 ', '/2019 ').replace('/', '-').replace(time,
                                                                                                        time)


tsvDirectory = "D:\\Programming\\_databases\\fitbitDateReformatting\\"


def reformatAllFiles():
    for file in glob.glob(tsvDirectory + "main_*.tsv"):
        lineTrack = 1
        with open(file) as tsvInFile, \
                open(file.replace('.tsv', '_reformatted.tsv').replace('main_', 'main-'), 'w') as tsvOutFile:
            for line in tsvInFile:
                if line.split('\t')[0].__len__() != 10:
                    sys.stdout.write(f"\rNow processing file::{file} line#::{lineTrack}")
                    tsvOutFile.write(yearReplace(line))
                    lineTrack += 1


if __name__ == '__main__':
    reformatAllFiles()
