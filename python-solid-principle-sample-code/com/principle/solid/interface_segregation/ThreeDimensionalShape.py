from abc import ABC, abstractmethod

"""
    Interface Segregation Principle Achieved - Created separate Interface for Add-On Feature into Existing Application. 
"""


class ThreeDimensionalShape(ABC):

    @abstractmethod
    def volume(self):
        pass
