from FileInterface import FileInterface
from RealFile import RealFile
class FileProxy(FileInterface):
    """Proxy class for loading and displaying a file."""
    
    def __init__(self, real_file: RealFile)-> None:
        self._real_file = real_file
        self.data = None

    def display(self)-> None:
        """Display the file content, loading it if necessary."""
        if self.data is None:
            self.data = self._real_file.display()
        else:
            print("FileProxy::display(): File content already loaded. Displaying cached content...")
            print(f"Cached content: {self.data}")