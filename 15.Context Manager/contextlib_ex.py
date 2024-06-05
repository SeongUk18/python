from contextlib import contextmanager


@contextmanager
def managed_file(filename):
    file = open(filename, 'w')
    try:
        yield file
    finally:
        file.close()

# 사용 예제
with managed_file('example.txt') as f:
    f.write('Hello, World!')

# 'example.txt' 파일은 with 블록이 끝나면 자동으로 닫힌다.
