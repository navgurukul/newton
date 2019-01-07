```ngMeta
name: checking-for-errors
```
# Checking for Errors
As you’ve seen, the Response object has a status_code attribute that can be checked against requests.codes.ok to see whether the download succeeded. A simpler way to check for success is to call the raise_for_status() method on the Response object. This will raise an exception if there was an error downloading the file and will do nothing if the download succeeded. Enter the following into the interactive shell:

```python
>>> res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
>>> res.raise_for_status()
```
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    res.raise_for_status()
  File "C:\Python34\lib\site-packages\requests\models.py", line 773, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found
The raise_for_status() method is a good way to ensure that a program halts if a bad download occurs. This is a good thing: You want your program to stop as soon as some unexpected error happens. If a failed download isn’t a deal breaker for your program, you can wrap the raise_for_status() line with try and except statements to handle this error case without crashing.


import requests
res = requests.get('<span><a href="http://inventwithpython.com/page_that_does_not_exist'">http://inventwithpython.com/page_that_does_not_exist'</a></span>)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
This raise_for_status() method call causes the program to output the following:


There was a problem: 404 Client Error: Not Found
Always call raise_for_status() after calling requests.get(). You want to be sure that the download has actually worked before your program continues.