"""
Iterate over half second intervals.
"""
from interval_timer import interval_timer


for interval in interval_timer(0.5):
    print(interval)
