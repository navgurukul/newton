```ngMeta
fetching-an-email-and-marking-it-as-read_key1
```
# fetching-an-email-and-marking-it-as-read_key2
fetching-an-email-and-marking-it-as-read_key3

fetching-an-email-and-marking-it-as-read_key4

fetching-an-email-and-marking-it-as-read_key5

```python
>>> rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
>>> import pprint
>>> pprint.pprint(rawMessages)
```
fetching-an-email-and-marking-it-as-read_key6[fetching-an-email-and-marking-it-as-read_key7](mailto:&#x6d;&#x79;&#x5f;&#101;&#109;&#97;&#x69;&#108;&#95;&#97;&#100;&#100;&#x72;&#101;&#115;&#x73;&#64;&#x67;&#109;&#x61;&#x69;&#x6c;&#46;&#99;&#x6f;&#x6d;)
fetching-an-email-and-marking-it-as-read_key8```python
>>> imapObj.select_folder('INBOX', readonly=False)
```
