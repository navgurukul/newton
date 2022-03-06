```ngMeta
name: connecting-to-an-smtp-server
```
# Connecting to an SMTP Server
If you’ve ever set up Thunderbird, Outlook, or another program to connect to your email account, you may be familiar with configuring the SMTP server and port. These settings will be different for each email provider, but a web search for <your provider> smtp settings should turn up the server and port to use.

The domain name for the SMTP server will usually be the name of your email provider’s domain name, with smtp. in front of it. For example, Gmail’s SMTP server is at smtp.gmail.com. Table 16-1 lists some common email providers and their SMTP servers. (The port is an integer value and will almost always be 587, which is used by the command encryption standard, TLS.)

Table 16-1. Email Providers and Their SMTP Servers

Provider 							SMTP server domain name

Gmail 								smtp.gmail.com

Outlook.com/Hotmail.com 			smtp-mail.outlook.com

Yahoo Mail 							smtp.mail.yahoo.com

AT&T 								smpt.mail.att.net (port 465)

Comcast 							smtp.comcast.net

Verizon								smtp.verizon.net (port 465)

Once you have the domain name and port information for your email provider, create an SMTP object by calling smptlib.SMTP(), passing the domain name as a string argument, and passing the port as an integer argument. The SMTP object represents a connection to an SMTP mail server and has methods for sending emails. For example, the following call creates an SMTP object for connecting to Gmail:
```python
>>> smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
>>> type(smtpObj)
```
<class 'smtplib.SMTP'>
Entering type(smtpObj) shows you that there’s an SMTP object stored in smtpObj. You’ll need this SMTP object in order to call the methods that log you in and send emails. If the smptlib.SMTP() call is not successful, your SMTP server might not support TLS on port 587. In this case, you will need to create an SMTP object using smtplib.SMTP_SSL() and port 465 instead.

```python
>>> smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
```
# Note
If you are not connected to the Internet, Python will raise a socket.gaierror: [Errno 11004] getaddrinfo failed or similar exception.

For your programs, the differences between TLS and SSL aren’t important. You only need to know which encryption standard your SMTP server uses so you know how to connect to it. In all of the interactive shell examples that follow, the smtpObj variable will contain an SMTP object returned by the smtplib.SMTP() or smtplib.SMTP_SSL() function.