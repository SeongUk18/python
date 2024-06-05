class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# 사용 예제
with ManagedFile('example.txt') as f:
    f.write('Hello, World!')

# 'example.txt' 파일은 with 블록이 끝나면 자동으로 닫힌다.
