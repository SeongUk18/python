# 텍스트 파일 읽기
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

with open('example.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())  # strip()을 사용하여 줄바꿈 문자 제거

# 텍스트 파일 쓰기
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, World!\n')

lines = ['First line\n', 'Second line\n', 'Third line\n']
with open('example.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines)

# 파일 업데이트하기
# 파일 끝에 내용 추가
with open('example.txt', 'a', encoding='utf-8') as file:
    file.write('Another line\n')

# 파일 처리 중 발생할 수 있는 예외 처리
try:
    with open('example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
except Exception as e:
    print(f"오류 발생: {e}")
