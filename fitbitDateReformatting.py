import glob
import csv
import sys


def yearReplace(dateTimeID: str) -> str:
    return dateTimeID.replace('/18 ', '/2018 ').replace('/19 ', '/2019 ')


tsvDirectory = "D:\\Programming\\_databases\\fitbitDateReformatting\\"

for file in glob.glob(tsvDirectory + "main_*.tsv"):
    lineTrack = 1
    with open(file) as tsvInFile, \
            open(file.replace('.tsv', '_reformatted.tsv').replace('main_', 'main-'), 'w') as tsvOutFile:
        for line in tsvInFile:
            sys.stdout.write(f"\rNow processing file::{file} line#::{lineTrack}")
            tsvOutFile.write(yearReplace(line))
            lineTrack += 1
