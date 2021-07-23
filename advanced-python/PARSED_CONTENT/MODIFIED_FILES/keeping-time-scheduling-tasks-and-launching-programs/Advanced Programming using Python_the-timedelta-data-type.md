```ngMeta
the-timedelta-data-type_key1
```

the-timedelta-data-type_key2
the-timedelta-data-type_key3


```python
❶ >>> delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
❷ >>> delta.days, delta.seconds, delta.microseconds
```
the-timedelta-data-type_key4
```python
   >>> delta.total_seconds()
```
the-timedelta-data-type_key5
```python
   >>> str(delta)
```
the-timedelta-data-type_key6


the-timedelta-data-type_key7


the-timedelta-data-type_key8
```python
>>> dt = datetime.datetime.now()
>>> dt
```
the-timedelta-data-type_key9
```python
>>> thousandDays = datetime.timedelta(days=1000)
>>> dt + thousandDays
```
the-timedelta-data-type_key10


the-timedelta-data-type_key11


```python
❶ >>> oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
❷ >>> aboutThirtyYears = datetime.timedelta(days=365 * 30)
   >>> oct21st
```
the-timedelta-data-type_key12
```python
   >>> oct21st - aboutThirtyYears
```
the-timedelta-data-type_key13
```python
   >>> oct21st - (2 * aboutThirtyYears)
```
the-timedelta-data-type_key14
