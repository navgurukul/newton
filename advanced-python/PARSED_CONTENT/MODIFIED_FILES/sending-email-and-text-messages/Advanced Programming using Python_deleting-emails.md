```ngMeta
deleting-emails_key1
```

deleting-emails_key2
deleting-emails_key3


```python
❶ >>> imapObj.select_folder('INBOX', readonly=False)
❷ >>> UIDs = imapObj.search(['ON 09-Jul-2015'])
   >>> UIDs
```
deleting-emails_key4
```python
   >>> imapObj.delete_messages(UIDs)
```
deleting-emails_key5
```python
   >>> imapObj.expunge()
```
deleting-emails_key6
