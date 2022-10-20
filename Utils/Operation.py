class OperationResult:

    def __init__(self, success, result = None, message=""):
        self.success = success
        self.result = result
        self.message = message

    @classmethod
    def CreateSuccess(self, result):
        return OperationResult(True,result,"")

    @classmethod
    def CreateError(self, errorMessage):
        return OperationResult(False,None,errorMessage)

    def OnSuccess(self, successCallback):
        if self.success:
            successCallback(self.result)
        return self

    def OnError(self, errorCallback):
        if not self.success:
            errorCallback(self.message)
        return self