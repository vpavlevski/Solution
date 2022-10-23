def array_has_exactly(parameter, numberOfElements):
    if len(parameter)==numberOfElements:
        return
    raise Exception("Array has " + str(len(parameter)) + " elements. It is expected to have: " + str(numberOfElements))