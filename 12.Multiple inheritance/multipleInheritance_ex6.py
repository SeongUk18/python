from abc import ABC, abstractmethod


class LoggingMixin:
    def log(self, message):
        print(f"Log: {message}")


class AbstractWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(LoggingMixin, AbstractWorker):
    def work(self):
        self.log("Working")


worker = Worker()
worker.work()  # "Log: Working" 출력
