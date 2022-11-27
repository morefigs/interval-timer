from __future__ import annotations
from typing import Optional
from time import sleep, perf_counter

from interval_timer.interval import Interval


class IntervalTimer:
    # Affects timer precision, but also prevents high CPU usage
    CPU_SLEEP_S = 0.0001

    def _time(self) -> float:
        """
        Get the time relative to the interval timer starting, in seconds.
        """
        time_abs = perf_counter()

        # Set time 0 on first interval creation
        if self._time_zero is None:
            self._time_zero = time_abs

        return time_abs - self._time_zero

    def __init__(self, period: float, start: int = 0, stop: Optional[int] = None):
        """
        An interval timer iterator that synchronises iterations to within specific time intervals.

        The time taken for code execution within each iteration will not affect the interval timing, provided that the
        execution time is not longer than the interval period. The caller can check if this is the case by checking the
        `missed` attribute on the returned `Interval` instance.

        :param period: The interval period, in seconds.
        :param start: The number of iterations to delay starting by.
        :param stop: The number of iterations to automatically stop after.
        """
        self._period: float = period
        self._index: int = start
        self._stop: int = stop
        self._time_zero: Optional[int] = None

    def __iter__(self) -> IntervalTimer:
        return self

    def __next__(self) -> Interval:
        if self._stop == self._index:
            raise StopIteration()

        interval = Interval(self._index, self._period, self._time())
        self._index += 1

        # Block the iteration until the interval begins
        while self._time() < interval.time:
            sleep(self.CPU_SLEEP_S)

        return interval


class IntervalError(Exception):
    pass
