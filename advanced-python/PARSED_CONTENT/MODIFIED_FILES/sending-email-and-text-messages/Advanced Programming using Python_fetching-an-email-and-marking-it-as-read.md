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
[fetching-an-email-and-marking-it-as-read_key6](mailto:&#109;&#121;&#95;&#101;&#109;&#x61;&#x69;&#x6c;&#95;&#x61;&#x64;&#x64;&#114;&#101;&#x73;&#x73;&#x40;&#103;&#109;&#97;&#x69;&#x6c;&#x2e;&#99;&#111;&#109;)
fetching-an-email-and-marking-it-as-read_key7
```python
>>> imapObj.select_folder('INBOX', readonly=False)
```