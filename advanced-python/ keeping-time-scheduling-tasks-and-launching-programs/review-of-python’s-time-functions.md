```ngMeta
name: review-of-python’s-time-functions
completionMethod: manual
```
# Review of Python’s Time Functions
Dates and times in Python can involve quite a few different data types and functions. Here’s a review of the three different types of values used to represent time:

A Unix epoch timestamp (used by the time module) is a float or integer value of the number of seconds since 12 AM on January 1, 1970, UTC.

A datetime object (of the datetime module) has integers stored in the attributes year, month, day, hour, minute, and second.

A timedelta object (of the datetime module) represents a time duration, rather than a specific moment.

Here’s a review of time functions and their parameters and return values:

The time.time() function returns an epoch timestamp float value of the current moment.

The time.sleep(seconds) function stops the program for the amount of seconds specified by the seconds argument.

The datetime.datetime(year, month, day, hour, minute, second) function returns a datetime object of the moment specified by the arguments. If hour, minute, or second arguments are not provided, they default to 0.

The datetime.datetime.now() function returns a datetime object of the current moment.

The datetime.datetime.fromtimestamp(epoch) function returns a datetime object of the moment represented by the epoch timestamp argument.

The datetime.timedelta(weeks, days, hours, minutes, seconds, milliseconds, microseconds) function returns a timedelta object representing a duration of time. The function’s keyword arguments are all optional and do not include month or year.

The total_seconds() method for timedelta objects returns the number of seconds the timedelta object represents.

The strftime(format) method returns a string of the time represented by the datetime object in a custom format that’s based on the format string. See Table 15-1 for the format details.

The datetime.datetime.strptime(time_string, format) function returns a datetime object of the moment specified by time_string, parsed using the format string argument. See Table 15-1 for the format details.