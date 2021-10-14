from time import time
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        self.start_time = None

    def __enter__(self):
        self.start_time = time()
        return

    def __exit__(self, *args):
        print("time:", time() - self.start_time)


@contextmanager
def cm_timer_2():
    start_time = time()
    yield
    print("time:", time() - start_time)
