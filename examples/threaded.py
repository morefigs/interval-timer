"""
Iterate asynchronously in a dedicated thread.
"""
from threading import Thread

from interval_timer import IntervalTimer


def threaded():
    for interval in IntervalTimer(0.25, stop=8):
        print(interval)


thread = Thread(target=threaded, daemon=True)
thread.start()

# Wait for thread to finish
thread.join()
