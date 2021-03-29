from abc import ABC, abstractmethod


class ABMI(ABC):
    @abstractmethod
    def bmi(self, weight: float, height: float):
        pass

    @abstractmethod
    def print_bmi(self, _bmi: float):
        pass