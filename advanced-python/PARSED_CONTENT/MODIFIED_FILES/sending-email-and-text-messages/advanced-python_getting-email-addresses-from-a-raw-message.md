```ngMeta
getting-email-addresses-from-a-raw-message_key1
```
# getting-email-addresses-from-a-raw-message_key2
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
getting-email-addresses-from-a-raw-message_key6```python
>>> message.get_addresses('from')
```
getting-email-addresses-from-a-raw-message_key7```python
>>> message.get_addresses('to')
```
getting-email-addresses-from-a-raw-message_key8[getting-email-addresses-from-a-raw-message_key9](mailto:&#x5f;&#x65;&#109;&#x61;&#105;&#108;&#95;&#97;&#100;&#x64;&#114;&#101;&#x73;&#115;&#x40;&#103;&#x6d;&#97;&#x69;&#x6c;&#46;&#x63;&#x6f;&#109;)
getting-email-addresses-from-a-raw-message_key10```python
>>> message.get_addresses('cc')
```
getting-email-addresses-from-a-raw-message_key11```python
>>> message.get_addresses('bcc')
```
getting-email-addresses-from-a-raw-message_key12