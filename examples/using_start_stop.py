"""
Iterate over 0.5 second intervals, delaying by 4 iterations and stopping at 8 iterations (including those skipped).
"""
from interval_timer import IntervalTimer


for interval in IntervalTimer(0.5, start=4, stop=8):
    print(interval)
