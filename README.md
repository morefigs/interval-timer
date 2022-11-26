# interval-timer

**interval-timer** is a Python package that enables iterating over a sequence of regular time intervals with high precision.


`IntervalTimer` is an iterator object that returns `Interval` objects at regular time intervals. Code can then be executed upon each time interval, and the intervals will stay synchronised even when the code execution time is non-zero.

As an example, `IntervalTimer` is a more precise replacement for a for loop that contains a wait. The following code:
    
```python
from time import sleep

# Iterates approximately every half second
for i in range(5):
    print(i)
    sleep(0.5)
```

can be replaced with:

```python
from interval_timer import IntervalTimer

# Iterates exactly every half second
for interval in IntervalTimer(0.5, stop=5):
    print(interval)
```

**interval-timer** uses [perf_counter](https://docs.python.org/3/library/time.html#time.perf_counter) under the hood to obtain high precision timing.

## Installation

Install from [PyPI](https://pypi.org/project/interval-timer/) via:

```shell
pip install interval-timer
```

## Usage

Basic usage is as follows:

```python
from interval_timer import IntervalTimer

for interval in IntervalTimer(0.5):
    print(interval)
    
    # Execute code exactly every half second here
    ...
```

Output:

```
Interval(index=0, time=0.000, lag=0.000)
Interval(index=1, time=0.500, lag=0.000)
Interval(index=2, time=1.000, lag=0.000)
...
```

For more usage examples see [examples/](examples).
