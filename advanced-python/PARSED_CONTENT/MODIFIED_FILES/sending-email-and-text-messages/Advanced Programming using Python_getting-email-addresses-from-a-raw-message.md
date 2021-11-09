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
[getting-email-addresses-from-a-raw-message_key8](mailto:&#x5f;&#101;&#109;&#97;&#105;&#x6c;&#x5f;&#97;&#x64;&#100;&#x72;&#x65;&#115;&#115;&#x40;&#x67;&#109;&#x61;&#x69;&#108;&#46;&#99;&#111;&#x6d;)
getting-email-addresses-from-a-raw-message_key9
```python
>>> message.get_addresses('cc')
```
getting-email-addresses-from-a-raw-message_key10
```python
>>> message.get_addresses('bcc')
```
getting-email-addresses-from-a-raw-message_key11
