import csv
from Utils.Operation import OperationResult

class CsvFileReader:

    def __init__(self, filePath):
        self.filePath = filePath
        self.isFileOpen = False

    def __enter__(self):
        try:
            self.csvFile = open(self.filePath, 'r')
            self.isFileOpen = True
            return OperationResult.CreateSuccess(self)
        except:
            return OperationResult.CreateError("Can not open CSV File")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.isFileOpen:
            self.csvFile.close()

    def ForEachLine(self, callBackFunction):
        csvReader = csv.reader(self.csvFile, delimiter=',')
        for row in csvReader:
            callBackFunction(row)