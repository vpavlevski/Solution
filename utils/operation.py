class OperationResult:

    def __init__(self, success, result = None, message=""):
        self.success = success
        self.result = result
        self.message = message

    @classmethod
    def create_success(self, result):
        return OperationResult(True,result,"")

    @classmethod
    def create_error(self, errorMessage):
        return OperationResult(False,None,errorMessage)

    def on_success(self, successCallback):
        if self.success:
            successCallback(self.result)
        return self

    def on_error(self, errorCallback):
        if not self.success:
            errorCallback(self.message)
        return self