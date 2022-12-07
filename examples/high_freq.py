"""
Iterate at precisely 100 Hz.
"""
from interval_timer import interval_timer, IntervalError


for interval in interval_timer(0.01):
    print(interval)

    if interval.lag:
        raise IntervalError('high iteration frequency could not be maintained')
