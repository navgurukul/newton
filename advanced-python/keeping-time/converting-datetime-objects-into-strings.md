```ngMeta
name: converting-datetime-objects-into-strings
```
# Converting datetime Objects into Strings
Epoch timestamps and datetime objects aren’t very friendly to the human eye. Use the strftime() method to display a datetime object as a string. (The f in the name of the strftime() function stands for format.)

The strftime() method uses directives similar to Python’s string formatting. Table 15-1 has a full list of strftime() directives.

Table 15-1. strftime() Directives

|strftime directive 	       |				Meaning                              |
|------------------------------|-----------------------------------------------------|
|%Y 						   |		Year with century, as in '2014'              |

%y 									Year without century, '00' to '99' (1970 to 2069)

%m 									Month as a decimal number, '01' to '12'

%B 									Full month name, as in 'November'

%b 									Abbreviated month name, as in 'Nov'

%d 									Day of the month, '01' to '31'

%j 									Day of the year, '001' to '366'

%w 									Day of the week, '0' (Sunday) to '6' (Saturday)

%A 									Full weekday name, as in 'Monday'

%a 									Abbreviated weekday name, as in 'Mon'

%H 									Hour (24-hour clock), '00' to '23'

%I 									Hour (12-hour clock), '01' to '12'

%M 									Minute, '00' to '59'

%S  								Second, '00' to '59'

%p 									'AM' or 'PM'

%%									Literal '%' character

Pass strrftime() a custom format string containing formatting directives (along with any desired slashes, colons, and so on), and strftime() will return the datetime object’s information as a formatted string. Enter the following into the interactive shell:

```python
>>> oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
>>> oct21st.strftime('%Y/%m/%d %H:%M:%S')
```
'2015/10/21 16:29:00'
```python
>>> oct21st.strftime('%I:%M %p')
```
'04:29 PM'
```python
>>> oct21st.strftime("%B of '%y")
```
"October of '15"
Here we have a datetime object for October 21, 2015 at 4:29 PM, stored in oct21st. Passing strftime() the custom format string '%Y/%m/%d %H:%M:%S' returns a string containing 2015, 10, and 21 separated by slahes and 16, 29, and 00 separated by colons. Passing '%I:%M% p' returns '04:29 PM', and passing "%B of '%y" returns "October of '15". Note that strftime() doesn’t begin with datetime.datetime.