import threading
import time


def worker():
    print("Starting worker")
    time.sleep(2)
    print("Worker done")


threads = []
for _ in range(5):
    thread = threading.Thread(target=worker)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


'''
Starting worker
Starting workerStarting worker

Starting worker
Starting worker
Worker doneWorker done
Worker done
Worker done

Worker done
'''