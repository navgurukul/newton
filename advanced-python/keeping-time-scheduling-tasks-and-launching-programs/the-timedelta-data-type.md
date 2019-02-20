```ngMeta
name: the-timedelta-data-type
```
# The timedelta Data Type
The datetime module also provides a timedelta data type, which represents a duration of time rather than a moment in time. Enter the following into the interactive shell:

```python
❶ >>> delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
❷ >>> delta.days, delta.seconds, delta.microseconds
```
   (11, 36548, 0)
```python
   >>> delta.total_seconds()
```
   986948.0
```python
   >>> str(delta)
```
   '11 days, 10:09:08'
To create a timedelta object, use the datetime.timedelta() function. The datetime.timedelta() function takes keyword arguments weeks, days, hours, minutes, seconds, milliseconds, and microseconds. There is no month or year keyword argument because “a month” or “a year” is a variable amount of time depending on the particular month or year. A timedelta object has the total duration represented in days, seconds, and microseconds. These numbers are stored in the days, seconds, and microseconds attributes, respectively. The total_seconds() method will return the duration in number of seconds alone. Passing a timedelta object to str() will return a nicely formatted, human-readable string representation of the object.

In this example, we pass keyword arguments to datetime.delta() to specify a duration of 11 days, 10 hours, 9 minutes, and 8 seconds, and store the returned timedelta object in delta ❶. This timedelta object’s days attributes stores 11, and its seconds attribute stores 36548 (10 hours, 9 minutes, and 8 seconds, expressed in seconds) ❷. Calling total_seconds() tells us that 11 days, 10 hours, 9 minutes, and 8 seconds is 986,948 seconds. Finally, passing the timedelta object to str() returns a string clearly explaning the duration.

The arithmetic operators can be used to perform date arithmetic on datetime values. For example, to calculate the date 1,000 days from now, enter the following into the interactive shell:
```python
>>> dt = datetime.datetime.now()
>>> dt
```
datetime.datetime(2015, 2, 27, 18, 38, 50, 636181)
```python
>>> thousandDays = datetime.timedelta(days=1000)
>>> dt + thousandDays
```
datetime.datetime(2017, 11, 23, 18, 38, 50, 636181)
First, make a datetime object for the current moment and store it in dt. Then make a timedelta object for a duration of 1,000 days and store it in thousandDays. Add dt and thousandDays together to get a datetime object for the date 1,000 days from now. Python will do the date arithmetic to figure out that 1,000 days after February 27, 2015, will be November 23, 2017. This is useful because when you calculate 1,000 days from a given date, you have to remember how many days are in each month and factor in leap years and other tricky details. The datetime module handles all of this for you.

timedelta objects can be added or subtracted with datetime objects or other timedelta objects using the + and - operators. A timedelta object can be multiplied or divided by integer or float values with the * and / operators. Enter the following into the interactive shell:

```python
❶ >>> oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
❷ >>> aboutThirtyYears = datetime.timedelta(days=365 * 30)
   >>> oct21st
```
   datetime.datetime(2015, 10, 21, 16, 29)
```python
   >>> oct21st - aboutThirtyYears
```
   datetime.datetime(1985, 10, 28, 16, 29)
```python
   >>> oct21st - (2 * aboutThirtyYears)
```
   datetime.datetime(1955, 11, 5, 16, 29)
Here we make a datetime object for October 21, 2015 ❶ and a timedelta object for a duration of about 30 years (we’re assuming 365 days for each of those years) ❷. Subtracting aboutThirtyYears from oct21st gives us a datetime object for the date 30 years before October 21, 2015. Subtracting 2 * aboutThirtyYears from oct21st returns a datetime object for the date 60 years before October 21, 2015.