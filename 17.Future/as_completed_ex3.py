import concurrent.futures
import time


def compute_square(n):
    if n == 3:
        raise ValueError("Intentional error for number 3")
    time.sleep(n)
    return n * n


numbers = [5, 4, 3, 2, 1]

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(compute_square, num) for num in numbers]

    for future in concurrent.futures.as_completed(futures, timeout=10):
        try:
            result = future.result()
        except concurrent.futures.TimeoutError:
            print("A task timed out")
        except Exception as exc:
            print(f"A task generated an exception: {exc}")
        else:
            print(f"Result: {result}")

'''
A task generated an exception: Intentional error for number 3
Result: 1
Result: 4
Result: 16
Result: 25
'''