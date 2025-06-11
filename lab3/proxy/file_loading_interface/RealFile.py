from FileInterface import FileInterface
from time import sleep

class RealFile(FileInterface):
    """Concrete class for loading and displaying a real file."""
    def __init__(self, data: str) -> None:
        self.data = data

    def display(self) -> str:
        """Display the file content, simulating a delay for loading."""
        self.loadFromDisk()
        print("RealFile::display(): Displaying file content...")
        print(f"RealFile::display(): File content: {self.data}")
        return self.data

    
    def loadFromDisk(self) -> None:
        """Simulate loading the file from disk."""
        print("RealFile::loadFromDisk(): Loading file from disk...")
        sleep(3)  # Simulate a delay for loading the file
        print("RealFile::loadFromDisk(): File loaded from disk successfully.") 
    