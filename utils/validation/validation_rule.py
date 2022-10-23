from abc import ABC, abstractmethod


class ValidationRule(ABC):

    @abstractmethod
    def execute(self, parameter):
        pass