from Shape import Shape
from typing import List
from abc import ABC, abstractmethod


class IAreaCalculator(ABC):

    @abstractmethod
    def sum(self, shapes: List[Shape]):
        pass
