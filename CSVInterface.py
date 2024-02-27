# Generic class interface for any file.
# 27/02/2024

from FileInterface import FileInterface
import csv

class CSVInterface(FileInterface):
    def read(self, fileName):
        data = []
        with open(fileName, "r") as file:
            reader = csv.reader(file)

            headers = next(reader) # (Stephen) Used to grab the headers from the file.
            for row in reader:
                headerIndex = 0
                rowDict = {}
                for rowData in row:
                    rowDict[headers[headerIndex]] = rowData
                    headerIndex = headerIndex + 1
                data.append(rowDict)
        return data

    # (Sam) Data should be structed in key/value pairs.
    # (Sam) e.g {{Value1 = "this", Value2 = "that"}}
    def write(self, fileName, data):
        with open(fileName, "w") as file:
            writer = csv.writer(file)
            keys = data.keys()
            writer.writerrow(keys)
            for row in data:
                newArr = []
                for key in keys:
                    newArr.append(row[key])
                writer.writerow(data)
