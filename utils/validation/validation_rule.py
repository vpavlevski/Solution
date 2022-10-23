from abc import ABC, abstractmethod


class ValidationRule(ABC):

    @abstractmethod
    def Execute(self, parameter):
        pass