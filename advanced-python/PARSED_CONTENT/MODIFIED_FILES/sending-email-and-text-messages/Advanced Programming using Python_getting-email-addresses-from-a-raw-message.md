```ngMeta
getting-email-addresses-from-a-raw-message_key1
```

getting-email-addresses-from-a-raw-message_key2
getting-email-addresses-from-a-raw-message_key3


getting-email-addresses-from-a-raw-message_key4


```python
>>> import pyzmail
>>> message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
```
getting-email-addresses-from-a-raw-message_key5


```python
>>> message.get_subject()
```
getting-email-addresses-from-a-raw-message_key6
```python
>>> message.get_addresses('from')
```
getting-email-addresses-from-a-raw-message_key7
```python
>>> message.get_addresses('to')
```
getting-email-addresses-from-a-raw-message_key8
```python
>>> message.get_addresses('cc')
```
getting-email-addresses-from-a-raw-message_key9
```python
>>> message.get_addresses('bcc')
```
getting-email-addresses-from-a-raw-message_key10
