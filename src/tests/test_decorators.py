import unittest
import decorators


class TestDecorators(unittest.TestCase):
    def test_loop_run_once(self):
        executed = 0

        @decorators.loop_run_once
        def execute():
            nonlocal executed
            executed += 1

        for _ in range(1000):
            execute()

        self.assertEqual(executed, 1)


if __name__ == "__main__":
    unittest.main()
