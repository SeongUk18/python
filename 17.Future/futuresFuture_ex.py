import concurrent.futures
import time


def slow_function(seconds):
    time.sleep(seconds)
    return f"Completed after {seconds} seconds"


with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(slow_function, 3)
    print(future.done())  # False
    time.sleep(1)
    print(future.done())  # False
    result = future.result()  # This will block until the result is available
    print(result)  # Completed after 3 seconds
    