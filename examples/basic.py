"""
Iterate over exact 1-second intervals, despite loop execution taking up to 1 second.
"""
from time import sleep
from random import random

from interval_timer import IntervalTimer


for interval in IntervalTimer(1):
    print(interval)

    # Sleeps up to 1 second
    sleep(random())
