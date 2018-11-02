```ngMeta
name: disabling-logging
completionMethod: manual
```
# Disabling Logging
After you’ve debugged your program, you probably don’t want all these log messages cluttering the screen. The logging.disable() function disables these so that you don’t have to go into your program and remove all the logging calls by hand. You simply pass logging.disable() a logging level, and it will suppress all log messages at that level or lower. So if you want to disable logging entirely, just add logging.disable(logging.CRITICAL) to your program. For example, enter the following into the interactive shell:

```python
>>> import logging
>>> logging.basicConfig(level=logging.INFO, format=' %(asctime)s'
```
%(levelname)s - %(message)s')
```python
>>> logging.critical('Critical error! Critical error!')
```
2015-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!
```python
>>> logging.disable(logging.CRITICAL)
>>> logging.critical('Critical error! Critical error!')
>>> logging.error('Error! Error!')
```
Since logging.disable() will disable all messages after it, you will probably want to add it near the import logging line of code in your program. This way, you can easily find it to comment out or uncomment that call to enable or disable logging messages as needed.