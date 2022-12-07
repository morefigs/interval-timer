"""
Iterate over 1 second intervals that are delayed by slow code execution, stopping when the lag exceeds half a second.
"""
from time import sleep

from interval_timer import interval_timer, IntervalError


for interval in interval_timer(1):
    print(interval)

    if interval.lag > 0.5:
        raise IntervalError('too much iteration lag')

    # Wait longer than the interval time!
    sleep(1.1)
