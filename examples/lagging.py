"""
Iterate over 1 second intervals, stopping when the lag exceeds half a second.
"""
from time import sleep

from interval_timer import IntervalTimer


for interval in IntervalTimer(1):
    print(interval)

    if interval.lag > 0.5:
        raise StopIteration('Too much lag!')

    sleep(1.1)
