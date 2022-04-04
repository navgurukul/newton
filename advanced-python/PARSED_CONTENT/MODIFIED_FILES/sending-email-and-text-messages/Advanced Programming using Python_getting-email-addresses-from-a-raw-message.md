getting-email-addresses-from-a-raw-message_key1
getting-email-addresses-from-a-raw-message_key2


getting-email-addresses-from-a-raw-message_key3


```python
>>> import pyzmail
>>> message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
```
getting-email-addresses-from-a-raw-message_key4


```python
>>> message.get_subject()
```
getting-email-addresses-from-a-raw-message_key5
```python
>>> message.get_addresses('from')
```
getting-email-addresses-from-a-raw-message_key6
```python
>>> message.get_addresses('to')
```
getting-email-addresses-from-a-raw-message_key7
[getting-email-addresses-from-a-raw-message_key8](mailto:&#95;&#x65;&#x6d;&#x61;&#105;&#108;&#95;&#97;&#100;&#100;&#x72;&#x65;&#x73;&#x73;&#x40;&#x67;&#109;&#97;&#x69;&#108;&#46;&#99;&#x6f;&#x6d;)
getting-email-addresses-from-a-raw-message_key9
```python
>>> message.get_addresses('cc')
```
getting-email-addresses-from-a-raw-message_key10
```python
>>> message.get_addresses('bcc')
```
getting-email-addresses-from-a-raw-message_key11
