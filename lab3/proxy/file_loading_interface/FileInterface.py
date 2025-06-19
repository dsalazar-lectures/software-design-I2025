from abc import ABC, abstractmethod
class FileInterface(ABC):
    """Abstract base class for file loading."""
    @abstractmethod
    def display(self)-> None:
        """Display the file content."""
        pass

