"""
Iterate at precisely 100 Hz.
"""
from interval_timer import IntervalTimer, IntervalError


for interval in IntervalTimer(0.01):
    print(interval)

    if interval.lag:
        raise IntervalError('high iteration frequency could not be maintained')
