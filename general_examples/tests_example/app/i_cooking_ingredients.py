from abc import ABC, abstractmethod

class ICookingIngredients(ABC) :
    @abstractmethod
    def get_name() -> str:
        None
    
    @abstractmethod
    def get_quantity() -> float:
        None
    
    @abstractmethod
    def get_quality() -> str:
        None
    