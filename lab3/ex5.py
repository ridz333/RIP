import time


class timer():
    def __init__(self):
        self.script_time = 0

    def __enter__(self):
        self.script_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self.script_time)
        self.script_time = 0


with timer():
    time.sleep(0.5)
    print('Времени потребовалось:')