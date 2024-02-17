from typing import Callable


def loop_run_once(function: Callable[[], None]):
    already_run = False

    def wrapper():
        nonlocal already_run
        if not already_run:
            function()
            already_run = True

    return wrapper
