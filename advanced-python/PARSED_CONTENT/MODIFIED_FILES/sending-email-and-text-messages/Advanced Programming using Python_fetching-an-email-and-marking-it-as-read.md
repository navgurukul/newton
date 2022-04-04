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
[fetching-an-email-and-marking-it-as-read_key6](mailto:&#x6d;&#121;&#x5f;&#101;&#x6d;&#97;&#x69;&#x6c;&#95;&#x61;&#100;&#100;&#x72;&#101;&#115;&#x73;&#64;&#x67;&#109;&#97;&#105;&#x6c;&#46;&#x63;&#111;&#x6d;)
fetching-an-email-and-marking-it-as-read_key7
```python
>>> imapObj.select_folder('INBOX', readonly=False)
```