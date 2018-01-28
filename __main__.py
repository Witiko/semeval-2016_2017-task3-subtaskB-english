"""This module produces SemEval Task 3, Subtask B datasets in JSON."""

from itertools import chain
from json import dump

from preprocessing import parse
from xmlfiles import XMLFiles

if __name__ == "__main__":
    result = {}
    for year, dataset in [(2016, "train"), (2016, "dev"), (2016, "test"), (2017, "test")]:
        with XMLFiles(year, dataset) as xmlfiles:
            result["%d-%s" % (year, dataset)] = list(chain(*[
                parse(xmlfile) for xmlfile in xmlfiles]))
    with open("result.json", "wb") as jsonfile:
        dump(result, jsonfile, sort_keys=True, indent=4)
