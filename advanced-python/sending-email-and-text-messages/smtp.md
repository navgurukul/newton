```ngMeta
name: smtp
completionMethod: manual
```
# SMTP
Much like HTTP is the protocol used by computers to send web pages across the Internet, Simple Mail Transfer Protocol (SMTP) is the protocol used for sending email. SMTP dictates how email messages should be formatted, encrypted, and relayed between mail servers, and all the other details that your computer handles after you click Send. You don’t need to know these technical details, though, because Python’s smtplib module simplifies them into a few functions.

SMTP just deals with sending emails to others. A different protocol, called IMAP, deals with retrieving emails sent to you and is described in IMAP.

# Sending Email
You may be familiar with sending emails from Outlook or Thunderbird or through a website such as Gmail or Yahoo! Mail. Unfortunately, Python doesn’t offer you a nice graphical user interface like those services. Instead, you call functions to perform each major step of SMTP, as shown in the following interactive shell example.

# Note
Don’t enter this example in IDLE; it won’t work because smtp.example.com, bob@example.com, MY_SECRET_PASSWORD, and alice@example.com are just placeholders. This code is just an overview of the process of sending email with Python.

```python
>>> import smtplib
>>> smtpObj = smtplib.SMTP('smtp.example.com', 587)
>>> smtpObj.ehlo()
```
(250, b'mx.example.com at your service, [216.172.148.131]\nSIZE 35882577\
n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
```python
>>> smtpObj.starttls()
```
(220, b'2.0.0 Ready to start TLS')
```python
>>> smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
```
(235, b'2.7.0 Accepted')
```python
>>> smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: Solong.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
{}
>>> smtpObj.quit()
```
(221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')
In the following sections, we’ll go through each step, replacing the placeholders with your information to connect and log in to an SMTP server, send an email, and disconnect from the server.