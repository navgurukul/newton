```ngMeta
name: don’t-debug-with-print()
```
# Don’t Debug with print()
Typing import logging and logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s') is somewhat unwieldy. You may want to use print() calls instead, but don’t give in to this temptation! Once you’re done debugging, you’ll end up spending a lot of time removing print() calls from your code for each log message. You might even accidentally remove some print() calls that were being used for nonlog messages. The nice thing about log messages is that you’re free to fill your program with as many as you like, and you can always disable them later by adding a single logging.disable(logging.CRITICAL) call. Unlike print(), the logging module makes it easy to switch between showing and hiding log messages.

Log messages are intended for the programmer, not the user. The user won’t care about the contents of some dictionary value you need to see to help with debugging; use a log message for something like that. For messages that the user will want to see, like File not found or Invalid input, please enter a number, you should use a print() call. You don’t want to deprive the user of useful information after you’ve disabled log messages.

# Logging Levels
Logging levels provide a way to categorize your log messages by importance. There are five logging levels, described in Table 10-1 from least to most important. Messages can be logged at each level using a different logging function.

Table 10-1. Logging Levels in Python

Level

Logging Function

Description

DEBUG

logging.debug()

The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.

INFO

logging.info()

Used to record information on general events in your program or confirm that things are working at their point in the program.

WARNING

logging.warning()

Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.

ERROR

logging.error()

Used to record an error that caused the program to fail to do something.

CRITICAL

logging.critical()

The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.

Your logging message is passed as a string to these functions. The logging levels are suggestions. Ultimately, it is up to you to decide which category your log message falls into. Enter the following into the interactive shell:

```python
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -'
%(levelname)s - %(message)s')'
>>> logging.debug('Some debugging details.')
```
2015-05-18 19:04:26,901 - DEBUG - Some debugging details.
```python
>>> logging.info('The logging module is working.')
```
2015-05-18 19:04:35,569 - INFO - The logging module is working.
```python
>>> logging.warning('An error message is about to be logged.')
```
2015-05-18 19:04:56,843 - WARNING - An error message is about to be logged.
```python
>>> logging.error('An error has occurred.')
```
2015-05-18 19:05:07,737 - ERROR - An error has occurred.
```python
>>> logging.critical('The program is unable to recover!')
```
2015-05-18 19:05:45,794 - CRITICAL - The program is unable to recover!
The benefit of logging levels is that you can change what priority of logging message you want to see. Passing logging.DEBUG to the basicConfig() function’s level keyword argument will show messages from all the logging levels (DEBUG being the lowest level). But after developing your program some more, you may be interested only in errors. In that case, you can set basicConfig()’s level argument to logging.ERROR. This will show only ERROR and CRITICAL messages and skip the DEBUG, INFO, and WARNING messages.

