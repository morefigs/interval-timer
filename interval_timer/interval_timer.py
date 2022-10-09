from typing import Optional
from time import sleep, perf_counter
from dataclasses import dataclass


@dataclass
class Interval:
    index: int
    period: float
    time_requested: float
    time: float

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(index={self.index}, time={self.time:.03f}, lag={self.lag:.03f})'

    @property
    def min(self) -> float:
        """
        The lower time limit of the interval.
        """
        return self.index * self.period

    @property
    def max(self) -> float:
        """
        The upper time limit of the interval.
        """
        return self.min + self.period

    @property
    def arrived(self) -> bool:
        """
        Whether this time interval has been reached.
        """
        return self.min <= self.time

    @property
    def missed(self) -> bool:
        """
        Indicates that the time interval was missed and (the start of) the iteration did not occur within the interval.
        """
        return self.max <= self.time

    @property
    def buffer(self) -> float:
        """
        The amount of time between the interval being requested and the interval starting. The minimum buffer is zero.
        """
        buffer = self.min - self.time_requested
        if buffer < 0:
            buffer = 0
        return buffer

    @property
    def lag(self) -> float:
        """
        The amount of time after the interval started and the interval being requested. The minimum lag is zero.
        """
        return self.time - self.min

    @property
    def buffer_percent(self) -> str:
        """
        Buffer as a percentage.
        """
        return f'{round(self.buffer / self.period * 100)}%'

    @property
    def lag_percent(self) -> str:
        """
        Lag as a percentage.
        """
        return f'{round(self.lag / self.period * 100)}%'


class IntervalTimer:
    # Affects timer precision, but also prevents high CPU usage
    CPU_THROTTLE_S = 0.0001

    def _perf_counter_relative(self) -> float:
        return perf_counter() - self._zero_count

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
        self._period = period
        self._index = start
        self._stop = stop
        self._zero_count = perf_counter()

    def __iter__(self) -> 'IntervalTimer':
        return self

    def __next__(self) -> Interval:
        if self._stop == self._index:
            raise StopIteration()

        time = self._perf_counter_relative()
        interval = Interval(self._index, self._period, time, time)

        # Block this iteration until the interval is arrived at
        while not interval.arrived:
            interval.time = self._perf_counter_relative()
            sleep(self.CPU_THROTTLE_S)

        self._index += 1
        return interval
