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
[fetching-an-email-and-marking-it-as-read_key6](mailto:&#109;&#121;&#x5f;&#x65;&#x6d;&#x61;&#x69;&#108;&#x5f;&#x61;&#x64;&#100;&#114;&#101;&#115;&#x73;&#x40;&#x67;&#x6d;&#97;&#x69;&#x6c;&#46;&#x63;&#111;&#109;)
fetching-an-email-and-marking-it-as-read_key7
```python
>>> imapObj.select_folder('INBOX', readonly=False)
```