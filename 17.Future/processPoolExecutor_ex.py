import concurrent.futures
import os


def compute_square(n):
    print(f"Process ID: {os.getpid()} computing {n} * {n}")
    return n * n


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    # ProcessPoolExecutor를 사용하여 병렬로 작업 실행
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        # 작업 제출
        futures = [executor.submit(compute_square, num) for num in numbers]

        # 결과 가져오기
        for future in concurrent.futures.as_completed(futures):
            print(f"Result: {future.result()}")

'''
Process ID: 3280 computing 1 * 1
Process ID: 3280 computing 2 * 2
Process ID: 3280 computing 3 * 3
Process ID: 3280 computing 4 * 4
Process ID: 3280 computing 5 * 5
Result: 1
Result: 4
Result: 9
Result: 16
Result: 25
'''