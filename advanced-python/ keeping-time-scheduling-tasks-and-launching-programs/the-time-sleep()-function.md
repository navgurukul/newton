```ngMeta
name: the-time-sleep()-function
completionMethod: manual
```
# The time.sleep() Function
If you need to pause your program for a while, call the time.sleep() function and pass it the number of seconds you want your program to stay paused. Enter the following into the interactive shell:

```python
   >>> import time
   >>> for i in range(3):
❶         print('Tick')
❷         time.sleep(1)
❸         print('Tock')
❹         time.sleep(1)
```
   Tick
   Tock
   Tick
   Tock
   Tick
   Tock
```python
❺ >>> time.sleep(5)
```
The for loop will print Tick ❶, pause for one second ❷, print Tock ❸, pause for one second ❹, print Tick, pause, and so on until Tick and Tock have each been printed three times.

The time.sleep() function will block—that is, it will not return and release your program to execute other code—until after the number of seconds you passed to time.sleep() has elapsed. For example, if you enter time.sleep(5) ❺, you’ll see that the next prompt (>>>) doesn’t appear until five seconds have passed.

Be aware that pressing CTRL-C will not interrupt time.sleep() calls in IDLE. IDLE waits until the entire pause is over before raising the KeyboardInterrupt exception. To work around this problem, instead of having a single time.sleep(30) call to pause for 30 seconds, use a for loop to make 30 calls to time.sleep(1).

```python
>>> for i in range(30):
```
    time.sleep(1)
If you press CTRL-C sometime during these 30 seconds, you should see the KeyboardInterrupt exception thrown right away.

