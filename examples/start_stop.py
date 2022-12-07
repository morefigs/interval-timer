"""
Iterate over half second intervals, delaying by 4 iterations and stopping after 8 iterations (including those skipped).
"""
from interval_timer import interval_timer


for interval in interval_timer(0.5, start=4, stop=8):
    print(interval)
