class StringArray:
    def __init__(self, strings):
        self.array = strings

    def ForEachLine(self, callback):
        for line in self.array:
            callback(line)

    def Count(self):
        return len(self.array)