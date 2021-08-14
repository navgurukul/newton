fetching-an-email-and-marking-it-as-read_key1
fetching-an-email-and-marking-it-as-read_key2


fetching-an-email-and-marking-it-as-read_key3


fetching-an-email-and-marking-it-as-read_key4


```python
>>> rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
>>> import pprint
>>> pprint.pprint(rawMessages)
```
fetching-an-email-and-marking-it-as-read_key5
```python
>>> imapObj.select_folder('INBOX', readonly=False)
```