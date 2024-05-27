from abc import ABC, abstractmethod


class FileSystemHandler(ABC):
    @abstractmethod
    def open(self, filepath):
        pass

    @abstractmethod
    def read(self, filepath):
        pass

    @abstractmethod
    def write(self, filepath, data):
        pass


class LocalFileSystemHandler(FileSystemHandler):
    def open(self, filepath):
        return open(filepath, 'r')

    def read(self, filepath):
        with open(filepath, 'r') as file:
            return file.read()

    def write(self, filepath, data):
        with open(filepath, 'w') as file:
            file.write(data)


class RemoteFileSystemHandler(FileSystemHandler):
    def open(self, filepath):
        # 원격 파일 시스템에서 파일을 여는 로직
        pass

    def read(self, filepath):
        # 원격 파일 시스템에서 파일을 읽는 로직
        pass

    def write(self, filepath, data):
        # 원격 파일 시스템에 파일을 쓰는 로직
        pass


local_handler = LocalFileSystemHandler()
data = local_handler.read('local_file.txt')
print(data)
