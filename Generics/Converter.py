# (Sam) A generic class that gives a structure to our conversion classes
class Converter():
    def __init__(self, fileType):
        self.fileType = fileType
        self.converters = {}

    # (Sam) Converter should be a anonymous function that converts a file from input -> output
    def addConversion(self, convertTo, converter):
        self.converters[convertTo] = converter
    
    def convertFile(self, fileName, fileType):
        self.converters[fileType](fileName)
    
    def readFile(self, fileName):
        return # (Sam) To be overridden by the converter.