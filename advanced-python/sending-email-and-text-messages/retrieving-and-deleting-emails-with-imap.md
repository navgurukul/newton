```ngMeta
name:  retrieving-and-deleting-emails-with-imap
```
# Retrieving and Deleting Emails with IMAP
Finding and retrieving an email in Python is a multistep process that requires both the imapclient and pyzmail third-party modules. Just to give you an overview, here’s a full example of logging in to an IMAP server, searching for emails, fetching them, and then extracting the text of the email messages from them.

```python
>>> import imapclient
>>> imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
>>> imapObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
'my_email_address@gmail.com Jane Doe authenticated (Success)'
>>> imapObj.select_folder('INBOX', readonly=True)
>>> UIDs = imapObj.search(['SINCE 05-Jul-2014'])
>>> UIDs
```
[40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
```python
>>> rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
>>> import pyzmail
>>> message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
>>> message.get_subject()
```
'Hello!'
```python
>>> message.get_addresses('from')
```
[('Edward Snowden', 'esnowden@nsa.gov')]
```python
>>> message.get_addresses('to')
```
[(Jane Doe', 'jdoe@example.com')]
```python
>>> message.get_addresses('cc')
```
[]
```python
>>> message.get_addresses('bcc')
```
[]
```python
>>> message.text_part != None
```
True
```python
>>> message.text_part.get_payload().decode(message.text_part.charset)
```
'Follow the money.\r\n\r\n-Ed\r\n'
```python
>>> message.html_part != None
```
True
```python
>>> message.html_part.get_payload().decode(message.html_part.charset)
```
'<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-
Al<br></div>\r\n'
```python
>>> imapObj.logout()
```
You don’t have to memorize these steps. After we go through each step in detail, you can come back to this overview to refresh your memory.