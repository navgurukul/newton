```ngMeta
name: getting-email-addresses-from-a-raw-message
```
# Getting Email Addresses from a Raw Message
The raw messages returned from the fetch() method still aren’t very useful to people who just want to read their email. The pyzmail module parses these raw messages and returns them as PyzMessage objects, which make the subject, body, “To” field, “From” field, and other sections of the email easily accessible to your Python code.

Continue the interactive shell example with the following (using UIDs from your own email account, not the ones shown here):

```python
>>> import pyzmail
>>> message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
```
First, import pyzmail. Then, to create a PyzMessage object of an email, call the pyzmail.PyzMessage.factory() function and pass it the 'BODY[]' section of the raw message. Store the result in message. Now message contains a PyzMessage object, which has several methods that make it easy to get the email’s subject line, as well as all sender and recipient addresses. The get_subject() method returns the subject as a simple string value. The get_addresses() method returns a list of addresses for the field you pass it. For example, the method calls might look like this:

```python
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
[(Jane Doe', 'my_email_address@gmail.com')]
```python
>>> message.get_addresses('cc')
```
[]
```python
>>> message.get_addresses('bcc')
```
[]
Notice that the argument for get_addresses() is 'from', 'to', 'cc', or 'bcc'. The return value of get_addresses() is a list of tuples. Each tuple contains two strings: The first is the name associated with the email address, and the second is the email address itself. If there are no addresses in the requested field, get_addresses() returns a blank list. Here, the 'cc' carbon copy and 'bcc' blind carbon copy fields both contained no addresses and so returned empty lists.