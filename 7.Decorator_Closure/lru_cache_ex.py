from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# 첫 번째 호출에서는 계산을 수행
print(fib(10))  # 55

# 동일한 인수로 재호출 시 캐시된 결과를 사용
print(fib(10))  # 55 (재계산 없음)