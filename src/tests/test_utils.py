import time
import unittest
import utils


class UtilsTest(unittest.TestCase):
    def test_timestamp_zero(self):
        seconds, minutes, hours = utils.get_timestamp(time.perf_counter())
        self.assertEqual(seconds, 0)
        self.assertEqual(minutes, 0)
        self.assertEqual(hours, 0)

    def test_timestamp_time1(self):
        seconds, minutes, hours = utils.get_timestamp(
            start_time=time.perf_counter() - 60
        )
        self.assertEqual(seconds, 0)
        self.assertEqual(minutes, 1)
        self.assertEqual(hours, 0)

    def test_timestamp_time2(self):
        seconds, minutes, hours = utils.get_timestamp(
            start_time=time.perf_counter() - 3600
        )
        self.assertEqual(seconds, 0)
        self.assertEqual(minutes, 0)
        self.assertEqual(hours, 1)

    def test_timestamp_time3(self):
        seconds, minutes, hours = utils.get_timestamp(
            start_time=time.perf_counter() - 3661
        )
        self.assertEqual(seconds, 1)
        self.assertEqual(minutes, 1)
        self.assertEqual(hours, 1)

    def test_timestamp_invalid_input(self):
        invalid = time.perf_counter() + 1398831
        seconds, minutes, hours = utils.get_timestamp(invalid)
        self.assertEqual(seconds, 0)
        self.assertEqual(minutes, 0)
        self.assertEqual(hours, 0)


if __name__ == "__main__":
    unittest.main()
