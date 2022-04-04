```ngMeta
name: pausing-until-a-specific-date
```
# Pausing Until a Specific Date
The time.sleep() method lets you pause a program for a certain number of seconds. By using a while loop, you can pause your programs until a specific date. For example, the following code will continue to loop until Halloween 2016:

```python
import datetime
import time
halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)
```
The time.sleep(1) call will pause your Python program so that the computer doesn’t waste CPU processing cycles simply checking the time over and over. Rather, the while loop will just check the condition once per second and continue with the rest of the program after Halloween 2016 (or whenever you program it to stop).
