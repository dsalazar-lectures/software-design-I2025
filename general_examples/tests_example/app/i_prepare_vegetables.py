from abc import ABC, abstractmethod
from tests_example.app.models.vegetables import vegetable

class IPrepareVegetables(ABC) :
    @abstractmethod
    def WashVegetable(self, vegetables : vegetable) -> str:
        pass
    
    @abstractmethod
    def CutVegetable(self, vegetables : vegetable) -> bool:
        pass
    
    @abstractmethod
    def IsPrepare(self, vegetables : vegetable) -> bool:
        pass
    