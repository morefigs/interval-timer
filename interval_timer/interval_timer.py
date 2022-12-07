from __future__ import annotations
from typing import Optional
from collections.abc import Iterator
from time import sleep

from stoppy import Stopwatch

from interval_timer.interval import Interval


# Affects timer precision, but also prevents high CPU usage
_CPU_SLEEP_S = 0.0001


def interval_timer(period: float, start: int = 0, stop: Optional[int] = None) -> Iterator[Interval]:
    """
    An interval timer iterator that synchronises iterations to within specific time intervals.

    The time taken for code execution within each iteration will not affect the interval timing, provided that the
    execution time is not longer than the interval period. The caller can check if this is the case by checking the
    `missed` attribute on the returned `Interval` instance.

    :param period: The interval period, in seconds.
    :param start: The number of iterations to delay starting by.
    :param stop: The number of iterations to automatically stop after.
    """
    index = start

    with Stopwatch() as stopwatch:
        while True:
            if stop is not None and index >= stop:
                return

            # Starts the stopwatch on first call, guaranteeing that the first call of stopwatch.time returns 0
            count = Interval(index, period, stopwatch.time(True))
            index += 1

            # Block the iteration until the next count time
            while stopwatch.time() < count.time:
                sleep(_CPU_SLEEP_S)

            yield count


class IntervalError(Exception):
    pass
