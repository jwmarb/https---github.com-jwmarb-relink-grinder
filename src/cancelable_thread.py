import threading
from typing import Callable


class CancelableThread(threading.Thread):
    def __init__(self, target: Callable[[Callable[[], bool]], None]):
        self._stopped = True
        threading.Thread.__init__(self, target=lambda: target(self.is_stopped))

    def stop(self):
        self._stopped = True

    def is_stopped(self):
        return self._stopped

    def start(self):
        self._stopped = False
        threading.Thread.start(self)
