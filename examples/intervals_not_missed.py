"""
Iterate over 1 second intervals forever, despite loop execution taking almost 1 second.
"""
from time import sleep

from interval_timer import IntervalTimer


for interval in IntervalTimer(1):
    print(interval.index, f'{interval.time:.03f}')
    sleep(0.9)
