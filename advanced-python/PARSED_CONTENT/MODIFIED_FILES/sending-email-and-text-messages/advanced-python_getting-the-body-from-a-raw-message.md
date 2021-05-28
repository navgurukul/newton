```ngMeta
getting-the-body-from-a-raw-message_key1
```
# getting-the-body-from-a-raw-message_key2
getting-the-body-from-a-raw-message_key3

getting-the-body-from-a-raw-message_key4

getting-the-body-from-a-raw-message_key5

```python
❶ >>> message.text_part != None
```
getting-the-body-from-a-raw-message_key6```python
   >>> message.text_part.get_payload().decode(message.text_part.charset)
```
getting-the-body-from-a-raw-message_key7```python
❸ >>> message.html_part != None
```
getting-the-body-from-a-raw-message_key8```python
❹ >>> message.html_part.get_payload().decode(message.html_part.charset)
```
getting-the-body-from-a-raw-message_key9getting-the-body-from-a-raw-message_key10getting-the-body-from-a-raw-message_key11getting-the-body-from-a-raw-message_key12