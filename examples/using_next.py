"""
Iterate over 1 second intervals using next().
"""
from interval_timer import IntervalTimer


timer = IntervalTimer(1)

next(timer)
next(timer)
interval = next(timer)
print(interval)
