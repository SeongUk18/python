import time
import functools

def log_function_data(func):
    """데커레이터 함수: 실행 시간, 인수, 반환값을 로그로 출력함."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 함수 실행 시작 시간
        result = func(*args, **kwargs)  # 함수 호출 및 결과 저장
        end_time = time.time()  # 함수 실행 종료 시간
        duration = end_time - start_time  # 실행 시간 계산
        # 로그 출력
        print(f"Function {func.__name__!r} called with arguments {args} and kwargs {kwargs}")
        print(f"Returned value: {result}")
        print(f"Execution time: {duration:.6f} seconds")
        return result
    return wrapper