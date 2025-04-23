from abc import ABC, abstractmethod

class FileSystemItem(ABC):
    @abstractmethod
    def show(self):
        pass

class File(FileSystemItem):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show(self):
        print(f"File: {self.name}, Size: {self.size} bytes")

class Directory(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self):
        print(f"Directory: {self.name}")
        for item in self.items:
            item.show()

file1 = File("file1.txt", 1000)
file2 = File("file2.txt", 2000)
file3 = File("file3.txt", 3000)

dir1 = Directory("dir1")
dir2 = Directory("dir2")

dir1.add(file1)
dir1.add(file2)

dir2.add(file3)
dir2.add(dir1)

dir1.show()

dir2.show()