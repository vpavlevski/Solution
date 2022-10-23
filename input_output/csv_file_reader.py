import csv

from utils.collections.string_array import StringArray
from utils.operation import OperationResult

class CsvFileReader:

    def __init__(self, filePath):
        self.filePath = filePath
        self.isFileOpen = False

    def __enter__(self):
        try:
            self.csvFile = open(self.filePath, 'r')
            self.isFileOpen = True
            return OperationResult.create_success(self)
        except:
            return OperationResult.create_error("Can not open CSV File")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.isFileOpen:
            self.csvFile.close()

    def get_all_lines_as_string_array(self)->StringArray:
        lines=[]
        self.for_each_line(lambda line : lines.append(line))
        return StringArray(lines)

    def for_each_line(self, callBackFunction):
        csvReader = csv.reader(self.csvFile, delimiter=',')
        for row in csvReader:
            callBackFunction(row)