class LoggingMixin:
    def log(self, message):
        print(f"Log: {message}")


class Application(LoggingMixin):
    def run(self):
        self.log("Application is running")


app = Application()
app.run()  # "Log: Application is running" 출력
