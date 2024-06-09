import concurrent.futures


def square(n):
    return n * n


with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(square, 10)
    result = future.result()
    print(result)  # Output: 100
    