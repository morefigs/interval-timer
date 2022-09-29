"""
Iterate over 1 second intervals forever, but stopping if one of the intervals was missed due to slow code execution.
"""
from time import sleep
from random import random

from interval_timer import IntervalTimer


for interval in IntervalTimer(1):
    print(interval.index, f'{interval.time:.03f}')

    if interval.missed:
        raise StopIteration('This time interval was missed!')

    sleep(random() * 2)
