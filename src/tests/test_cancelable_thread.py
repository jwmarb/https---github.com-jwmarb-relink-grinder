import sys
import time
from typing import Callable
import unittest
from cancelable_thread import CancelableThread


class TestCancelableThread(unittest.TestCase):
    def test_thread_operation(self):
        def mock_target(is_stopped: Callable[[bool], None]):
            self.assertFalse(is_stopped())
            time.sleep(1)
            self.assertTrue(is_stopped())

        thread = CancelableThread(target=mock_target)
        thread.start()
        self.assertTrue(thread.is_alive())
        thread.stop()
        self.assertTrue(thread.is_stopped())
        self.assertTrue(thread.is_alive())
        thread.join()
        self.assertFalse(thread.is_alive())


if __name__ == "__main__":
    unittest.main()
