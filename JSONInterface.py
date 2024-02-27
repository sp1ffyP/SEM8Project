from FileInterface import FileInterface
import json

class JSONInterface(FileInterface):
    def read(self, fileName):
        data = {}
        with open(fileName, "r") as file:
            data = json.load(file)
        return data

    # (Sam) Data should be structed in key/value pairs.
    # (Sam) e.g {{Value1 = "this", Value2 = "that"}}
    def write(self, fileName, data):
        with open(fileName, "w") as file:
            json.dump(data, file)
