"""
Iterate over 1 second intervals forever.
"""
from interval_timer import IntervalTimer


for interval in IntervalTimer(1):
    print(interval.index, interval.time)
