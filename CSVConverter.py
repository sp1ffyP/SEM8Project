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
        print()
        print(data)

    def readFile(self, fileName):
        data = {}
        with open(fileName, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            header = []  # Used to get the column names from the first row
            header = next(reader)
            print(header)
            for row in reader:
                print(row)
                headerIndex = 0
                for rowData in row:
                    data[header[headerIndex]] = rowData
                    headerIndex = headerIndex + 1
        return data
