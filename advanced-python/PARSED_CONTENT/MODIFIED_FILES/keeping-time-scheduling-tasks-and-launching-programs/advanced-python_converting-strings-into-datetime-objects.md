```ngMeta
converting-strings-into-datetime-objects_key1
```
# converting-strings-into-datetime-objects_key2
converting-strings-into-datetime-objects_key3

converting-strings-into-datetime-objects_key4

```python
❶ >>> datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
   datetime.datetime(2015, 10, 21, 0, 0)
   >>> datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
   datetime.datetime(2015, 10, 21, 16, 29)
   >>> datetime.datetime.strptime("October of '15", "%B of '%y")
   datetime.datetime(2015, 10, 1, 0, 0)
   >>> datetime.datetime.strptime("November of '63", "%B of '%y")
```
converting-strings-into-datetime-objects_key5

