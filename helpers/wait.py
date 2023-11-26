import sys
import time
from typing import Any

import allure


def is_debugging() -> bool:
    """
    Determine if the code is running under a debugger

    :return: bool
    """
    return sys.gettrace() is not None


@allure.step("Wait for {waiting_for}")
def wait(
    waiting_for: str = None,
    condition: callable = None,
    timeout: int = 10,
    interval: int = 1,
) -> Any:
    """
    Wait until callable `condition` and return the result of the `condition`.
    :param waiting_for: description of what to wait for (it will be prefixed by '...waiting for ')
    :param condition: callable (function or lambda)
    :param timeout: total timeout, in seconds
    :param interval: time to sleep between tries, in seconds
    :return: the result of the `condition`
    """
    start_time = time.time()
    is_succeeded = False
    result = None
    last_call_error = None
    while not is_succeeded and time.time() - start_time < timeout:
        # We need to see in the assertion only the error that has happened in the last call of the `condition`,
        # so we reset the error in the start_time of each cycle
        last_call_error = None
        try:
            result = condition()
        except Exception as e:
            last_call_error = e

        if not result:
            time.sleep(interval)
        else:
            is_succeeded = True
            break

    if not is_succeeded:
        if not waiting_for:
            waiting_for = condition

        msg = (
            f'Timeout {timeout}s expired while waiting for "{waiting_for}".\n'
            f"Last error: {last_call_error}"
        )
        if not is_debugging():
            # Do not fail if the code is running under a debugger
            raise AssertionError(last_call_error, msg)

    return result
