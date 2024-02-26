import csv
import json
import os
from Converter import Converter

class CSVConverter(Converter):
    def __init__(self):
        super().__init__("CSV")
        self.addConversion("JSON", self.convertToJSON)

    def convertToJSON(self, fileName):
        data = self.readFile(fileName)

    def readFile(self, fileName):
        data = {}
        with open(fileName, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            header = []  # (Stephen) Used to get the column names from the first row
            header = next(reader)
            for row in reader:
                headerIndex = 0
                for rowData in row:
                    data[header[headerIndex]] = rowData
                    headerIndex = headerIndex + 1
        return data
