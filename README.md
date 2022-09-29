# interval-timer

An interval timer iterator that synchronises code execution to within specific time intervals.

The time taken for code execution within each iteration will not affect the interval timing, provided that the execution time is not longer than the interval period. The caller can check if this is the case by checking the `missed` attribute on the returned `Interval` instance.

## Installation

    pip install interval-timer

## Usage

    from interval_timer import IntervalTimer
    
    for interval in IntervalTimer(1):
        print(interval.index, interval.time)
        
        # Do time synchronised task once per second here...
