from dataclasses import dataclass


@dataclass
class Interval:
    index: int
    period: float
    _time_ready: float

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(index={self.index}, time={self.time:.03f}, lag={self.lag:.03f})'

    @property
    def time(self) -> float:
        """
        The start time of the interval, in seconds since the iterator object was created.
        """
        return self.index * self.period

    @property
    def buffer(self) -> float:
        """
        The length of time before the interval start time that the interval was requested. The minimum buffer is zero.
        """
        if self.time < self._time_ready:
            return 0
        return self.time - self._time_ready

    @property
    def lag(self) -> float:
        """
        The length of time after the interval start time that the interval was requested. The minimum lag is zero.

        If the lag is non-zero, then the code executed within the previous interval took longer than the interval
        period, which is generally undesirable.
        """
        if self._time_ready < self.time:
            return 0
        return self._time_ready - self.time
