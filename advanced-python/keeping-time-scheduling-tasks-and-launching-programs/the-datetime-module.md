```ngMeta
name: the-datetime-module
```
# The datetime Module
The time module is useful for getting a Unix epoch timestamp to work with. But if you want to display a date in a more convenient format, or do arithmetic with dates (for example, figuring out what date was 205 days ago or what date is 123 days from now), you should use the datetime module.

The datetime module has its own datetime data type. datetime values represent a specific moment in time. Enter the following into the interactive shell:

```python
   >>> import datetime
❶ >>> datetime.datetime.now()
❷ datetime.datetime(2015, 2, 27, 11, 10, 49, 55, 53)
❸ >>> dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
❹ >>> dt.year, dt.month, dt.day
   (2015, 10, 21)
❺ >>> dt.hour, dt.minute, dt.second
```
   (16, 29, 0)
Calling datetime.datetime.now() ❶ returns a datetime object ❷ for the current date and time, according to your computer’s clock. This object includes the year, month, day, hour, minute, second, and microsecond of the current moment. You can also retrieve a datetime object for a specific moment by using the datetime.datetime() function ❸, passing it integers representing the year, month, day, hour, and second of the moment you want. These integers will be stored in the datetime object’s year, month, day ❹, hour, minute, and second ❺ attributes.

A Unix epoch timestamp can be converted to a datetime object with the datetime.datetime.fromtimestamp() function. The date and time of the datetime object will be converted for the local time zone. Enter the following into the interactive shell:

```python
>>> datetime.datetime.fromtimestamp(1000000)
```
datetime.datetime(1970, 1, 12, 5, 46, 40)
```python
>>> datetime.datetime.fromtimestamp(time.time())
```
datetime.datetime(2015, 2, 27, 11, 13, 0, 604980)
Calling datetime.datetime.fromtimestamp() and passing it 1000000 returns a datetime object for the moment 1,000,000 seconds after the Unix epoch. Passing time.time(), the Unix epoch timestamp for the current moment, returns a datetime object for the current moment. So the expressions datetime.datetime.now() and datetime.datetime.fromtimestamp(time.time()) do the same thing; they both give you a datetime object for the present moment.

Note
These examples were entered on a computer set to Pacific Standard Time. If you’re in another time zone, your results will look different.

datetime objects can be compared with each other using comparison operators to find out which one precedes the other. The later datetime object is the “greater” value. Enter the following into the interactive shell:

```python
❶ >>> halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
❷ >>> newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
   >>> oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
❸ >>> halloween2015 == oct31_2015
```
   True
```python
❹ >>> halloween2015 > newyears2016
```
   False
```python
❺ >>> newyears2016 > halloween2015
```
   True
```python
   >>> newyears2016 != oct31_2015
```
   True
Make a datetime object for the first moment (midnight) of October 31, 2015 and store it in halloween2015 ❶. Make a datetime object for the first moment of January 1, 2016 and store it in newyears2016 ❷. Then make another object for midnight on October 31, 2015 and store it in oct31_2015. Comparing halloween2015 and oct31_2015 shows that they’re equal ❸. Comparing newyears2016 and halloween2015 shows that newyears2016 is greater (later) than halloween2015 ❹ ❺.

