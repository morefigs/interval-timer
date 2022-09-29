"""
Iterate over 1 second intervals, but stopping when one of the intervals was missed due to slow code execution.
"""
from time import sleep

from interval_timer import IntervalTimer


for interval in IntervalTimer(1):
    print(interval)

    if interval.missed:
        raise StopIteration('This time interval was missed!')

    sleep(1.2)
