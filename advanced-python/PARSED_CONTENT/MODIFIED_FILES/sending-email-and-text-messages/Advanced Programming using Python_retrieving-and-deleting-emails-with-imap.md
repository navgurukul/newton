```ngMeta
retrieving-and-deleting-emails-with-imap_key1
```

retrieving-and-deleting-emails-with-imap_key2
retrieving-and-deleting-emails-with-imap_key3


```python
>>> import imapclient
>>> imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
>>> imapObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
'my_email_address@gmail.com Jane Doe authenticated (Success)'
>>> imapObj.select_folder('INBOX', readonly=True)
>>> UIDs = imapObj.search(['SINCE 05-Jul-2014'])
>>> UIDs
```
retrieving-and-deleting-emails-with-imap_key4
```python
>>> rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
>>> import pyzmail
>>> message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
>>> message.get_subject()
```
retrieving-and-deleting-emails-with-imap_key5
```python
>>> message.get_addresses('from')
```
retrieving-and-deleting-emails-with-imap_key6
```python
>>> message.get_addresses('to')
```
retrieving-and-deleting-emails-with-imap_key7
```python
>>> message.get_addresses('cc')
```
retrieving-and-deleting-emails-with-imap_key8
```python
>>> message.get_addresses('bcc')
```
retrieving-and-deleting-emails-with-imap_key9
```python
>>> message.text_part != None
```
retrieving-and-deleting-emails-with-imap_key10
```python
>>> message.text_part.get_payload().decode(message.text_part.charset)
```
retrieving-and-deleting-emails-with-imap_key11
```python
>>> message.html_part != None
```
retrieving-and-deleting-emails-with-imap_key12
```python
>>> message.html_part.get_payload().decode(message.html_part.charset)
```
retrieving-and-deleting-emails-with-imap_key13
```python
>>> imapObj.logout()
```
retrieving-and-deleting-emails-with-imap_key14
