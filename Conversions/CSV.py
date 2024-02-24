import csv
import os
from Generics.Converter import Converter

class CSV(Converter):
    def __init__(self):
        super().__init__("CSV")
        self.addConversion("JSON", lambda fileName : {
            print("stub")
        })

    def readFile(self, fileName):
        with open(fileName, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = []  # Used to get the column names from the first row
            header = next(reader)
            print(header)
            for row in reader:
                print(row)
