import concurrent.futures
import time


def compute_square(n):
    time.sleep(n)
    return n * n


numbers = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(compute_square, num) for num in numbers]

        for future in concurrent.futures.as_completed(futures):
            print(f"Result: {future.result()}")

'''

'''