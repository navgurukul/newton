```ngMeta
the-datetime-module_key1
```
# the-datetime-module_key2
the-datetime-module_key3

the-datetime-module_key4

```python
   >>> import datetime
❶ >>> datetime.datetime.now()
❷ datetime.datetime(2015, 2, 27, 11, 10, 49, 55, 53)
❸ >>> dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
❹ >>> dt.year, dt.month, dt.day
   (2015, 10, 21)
❺ >>> dt.hour, dt.minute, dt.second
```
the-datetime-module_key5

the-datetime-module_key6

```python
>>> datetime.datetime.fromtimestamp(1000000)
```
the-datetime-module_key7```python
>>> datetime.datetime.fromtimestamp(time.time())
```
the-datetime-module_key8

the-datetime-module_key9

the-datetime-module_key10

```python
❶ >>> halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
❷ >>> newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
   >>> oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
❸ >>> halloween2015 == oct31_2015
```
the-datetime-module_key11```python
❹ >>> halloween2015 > newyears2016
```
the-datetime-module_key12```python
❺ >>> newyears2016 > halloween2015
```
the-datetime-module_key13```python
   >>> newyears2016 != oct31_2015
```
the-datetime-module_key14

