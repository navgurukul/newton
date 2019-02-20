```ngMeta
name:  getting-the-body-from-a-raw-message
```
# Getting the Body from a Raw Message
Emails can be sent as plaintext, HTML, or both. Plaintext emails contain only text, while HTML emails can have colors, fonts, images, and other features that make the email message look like a small web page. If an email is only plaintext, its PyzMessage object will have its html_part attributes set to None. Likewise, if an email is only HTML, its PyzMessage object will have its text_part attribute set to None.

Otherwise, the text_part or html_part value will have a get_payload() method that returns the email’s body as a value of the bytes data type. (The bytes data type is beyond the scope of this book.) But this still isn’t a string value that we can use. Ugh! The last step is to call the decode() method on the bytes value returned by get_payload(). The decode() method takes one argument: the message’s character encoding, stored in the text_part.charset or html_part.charset attribute. This, finally, will return the string of the email’s body.

Continue the interactive shell example by entering the following:

```python
❶ >>> message.text_part != None
```
   True
```python
   >>> message.text_part.get_payload().decode(message.text_part.charset)
```
❷ 'So long, and thanks for all the fish!\r\n\r\n-Al\r\n'
```python
❸ >>> message.html_part != None
```
   True
```python
❹ >>> message.html_part.get_payload().decode(message.html_part.charset)
```
   '<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al
   <br></div>\r\n'
The email we’re working with has both plaintext and HTML content, so the PyzMessage object stored in message has text_part and html_part attributes not equal to None ❶ ❸. Calling get_payload() on the message’s text_part and then calling decode() on the bytes value returns a string of the text version of the email ❷. Using get_payload() and decode() with the message’s html_part returns a string of the HTML version of the email ❹.