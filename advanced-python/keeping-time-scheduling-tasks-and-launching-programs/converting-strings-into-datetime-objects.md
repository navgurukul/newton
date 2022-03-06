```ngMeta
name: converting-strings-into-datetime-objects
```
# Converting Strings into datetime Objects
If you have a string of date information, such as '2015/10/21 16:29:00' or 'October 21, 2015', and need to convert it to a datetime object, use the datetime.datetime.strptime() function. The strptime() function is the inverse of the strftime() method. A custom format string using the same directives as strftime() must be passed so that strptime() knows how to parse and understand the string. (The p in the name of the strptime() function stands for parse.)

Enter the following into the interactive shell:

```python
❶ >>> datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
   datetime.datetime(2015, 10, 21, 0, 0)
   >>> datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
   datetime.datetime(2015, 10, 21, 16, 29)
   >>> datetime.datetime.strptime("October of '15", "%B of '%y")
   datetime.datetime(2015, 10, 1, 0, 0)
   >>> datetime.datetime.strptime("November of '63", "%B of '%y")
```
   datetime.datetime(2063, 11, 1, 0, 0)
To get a datetime object from the string 'October 21, 2015', pass 'October 21, 2015' as the first argument to strptime() and the custom format string that corresponds to 'October 21, 2015' as the second argument ❶. The string with the date information must match the custom format string exactly, or Python will raise a ValueError exception.

