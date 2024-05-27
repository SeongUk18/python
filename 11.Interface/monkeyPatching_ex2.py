import time


def slow_function():
    time.sleep(2)
    return "Original Function"


# 멍키 패칭을 사용하여 함수의 동작을 수정
def fast_function():
    return "Patched Function"


# 원래 함수 저장
original_function = slow_function

# 함수 교체
slow_function = fast_function

# 테스트
print(slow_function())  # 출력: Patched Function

# 원래 함수 복원
slow_function = original_function
print(slow_function())  # 출력: Original Function
