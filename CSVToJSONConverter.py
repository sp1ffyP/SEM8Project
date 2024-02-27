from CSVInterface import CSVInterface
from JSONInterface import JSONInterface
from pathlib import Path
import os
import csv

class CSVToJSONConverter():
    def __init__(self, inputDirectory, outputDirectory):
        self.inputDir = inputDirectory
        self.outputDir = outputDirectory

    def convert(self):
        files = os.listdir(self.inputDir)
        csvInterface = CSVInterface()
        jsonInterface = JSONInterface()
        for file in files:
            data = csvInterface.read(self.inputDir + "/" + file)
            rawName = Path(self.inputDir + "/" + file).stem
            print("  - " + rawName)
            jsonInterface.write(self.outputDir + "/" + rawName + ".json", data)
