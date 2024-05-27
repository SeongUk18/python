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


class LegacyFileHandler:
    def open(self, filepath):
        return open(filepath, 'r')

    def read(self, filepath):
        with open(filepath, 'r') as file:
            return file.read()

    def write(self, filepath, data):
        with open(filepath, 'w') as file:
            file.write(data)


# LegacyFileHandler를 FileSystemHandler의 가상 서브클래스로 등록
FileSystemHandler.register(LegacyFileHandler)

# 가상 서브클래스 확인
print(issubclass(LegacyFileHandler, FileSystemHandler))  # 출력: True

legacy_handler = LegacyFileHandler()
print(isinstance(legacy_handler, FileSystemHandler))  # 출력: True
