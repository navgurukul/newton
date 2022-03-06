```ngMeta
name: sending-the-smtp-“hello”-message
```
# Sending the SMTP “Hello” Message
Once you have the SMTP object, call its oddly named ehlo() method to “say hello” to the SMTP email server. This greeting is the first step in SMTP and is important for establishing a connection to the server. You don’t need to know the specifics of these protocols. Just be sure to call the ehlo() method first thing after getting the SMTP object or else the later method calls will result in errors. The following is an example of an ehlo() call and its return value:

```python
>>> smtpObj.ehlo()
```
(250, b'mx.google.com at your service, [216.172.148.131]\nSIZE 35882577\
n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
If the first item in the returned tuple is the integer 250 (the code for “success” in SMTP), then the greeting succeeded.
# Starting TLS Encryption
If you are connecting to port 587 on the SMTP server (that is, you’re using TLS encryption), you’ll need to call the starttls() method next. This required step enables encryption for your connection. If you are connecting to port 465 (using SSL), then encryption is already set up, and you should skip this step.

Here’s an example of the starttls() method call:

```python
>>> smtpObj.starttls()
```
(220, b'2.0.0 Ready to start TLS')
starttls() puts your SMTP connection in TLS mode. The 220 in the return value tells you that the server is ready.

