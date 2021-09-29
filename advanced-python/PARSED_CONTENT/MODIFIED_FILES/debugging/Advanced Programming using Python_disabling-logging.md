disabling-logging_key1
disabling-logging_key2


```python
>>> import logging
>>> logging.basicConfig(level=logging.INFO, format=' %(asctime)s'
```
disabling-logging_key3
```python
>>> logging.critical('Critical error! Critical error!')
```
disabling-logging_key4
```python
>>> logging.disable(logging.CRITICAL)
>>> logging.critical('Critical error! Critical error!')
>>> logging.error('Error! Error!')
```
disabling-logging_key5
