"""
Iterate over half second intervals.
"""
from interval_timer import IntervalTimer


for interval in IntervalTimer(0.5):
    print(interval)
