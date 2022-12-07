"""
Iterate asynchronously in a dedicated thread.
"""
from threading import Thread, current_thread

from interval_timer import interval_timer


def threaded():
    for interval in interval_timer(0.5, stop=4):
        print(f'{current_thread().name}: {interval}')


thread = Thread(target=threaded, daemon=True)
thread.start()

# Wait for thread to finish
thread.join()
