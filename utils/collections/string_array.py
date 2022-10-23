class StringArray:
    def __init__(self, strings):
        self.array = strings

    def for_each_line(self, callback):
        for line in self.array:
            callback(line)

    def count(self):
        return len(self.array)